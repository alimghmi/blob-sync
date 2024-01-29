from azure.storage.blob import BlobServiceClient

from config import logger


class Client:

    def __init__(
        self, file_exts: list, account_name: str, account_key: str, container_name: str
    ):
        self.file_exts = self.parse_file_exts(file_exts)
        self.container_name = container_name
        self.cnx_string = f"DefaultEndpointsProtocol=https;AccountName={account_name};AccountKey={account_key};EndpointSuffix=core.windows.net"  # noqa: E501
        self.__init_cnx()

    def __init_cnx(self):
        logger.info("Initializing connection to Azure Blob Storage")
        try:
            service_client = BlobServiceClient.from_connection_string(self.cnx_string)
            self.cnx = service_client.get_container_client(self.container_name)
            logger.info("Connection initialized successfully")
        except Exception as e:
            logger.error(f"Error initializing connection to Azure Blob Storage: {e}")
            raise

    def fetch(self) -> list:
        logger.info(f"Fetching blobs from container: {self.container_name}")
        blobs = self.cnx.list_blobs()
        blob_names = [blob.name for blob in blobs]
        if not self.file_exts:
            logger.debug(
                "No file extensions specified for filtering; returning all blob names."
            )
            return blob_names

        filtered_blob_names = [
            blob for blob in blob_names if self.matches_extension(blob)
        ]
        logger.debug(f"Filtered blob names based on extensions: {filtered_blob_names}")
        return filtered_blob_names

    def matches_extension(self, blob: str) -> bool:
        return any([blob.endswith(ext) for ext in self.file_exts])

    @staticmethod
    def parse_file_exts(file_exts: list) -> list:
        if not isinstance(file_exts, list):
            logger.error("file_exts must be a list.")
            raise ValueError("file_exts must be a list.")

        if "*" in file_exts or not len(file_exts):
            logger.debug(
                "Wildcard or empty file extensions list provided; no filtering will be applied."
            )
            return []
        else:
            file_exts = [
                (ext if ext.startswith(".") else f".{ext}") for ext in file_exts
            ]
            logger.debug(f"Parsed file extensions: {file_exts}")
            return file_exts
