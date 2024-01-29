from azure.storage.blob import BlobServiceClient


class Client:

    def __init__(
        self, file_exts: list, account_name: str, account_key: str, container_name: str
    ):
        self.file_exts = self.__parse_file_exts(file_exts)
        self.container_name = container_name
        self.cnx_string = f"DefaultEndpointsProtocol=https;AccountName={account_name};AccountKey={account_key};EndpointSuffix=core.windows.net"
        self.__init_cnx()

    def fetch(self) -> list:
        blobs = self.cnx.list_blobs()
        blob_names = [blob.name for blob in blobs]
        if not self.file_exts:
            return blob_names

        filtered_blob_names = [blob for blob in blob_names if self.check_ext(blob)]
        return filtered_blob_names

    def check_ext(self, blob: str) -> bool:
        return any([blob.endswith(ext) for ext in self.file_exts])

    def __init_cnx(self):
        service_client = BlobServiceClient.from_connection_string(self.cnx_string)
        self.cnx = service_client.get_container_client(self.container_name)
        return

    @staticmethod
    def __parse_file_exts(file_exts: list) -> list:
        if not isinstance(file_exts, list):
            raise ValueError("file_exts must be a list.")

        if "*" in file_exts or not len(file_exts):
            return []
        else:
            file_exts = [
                (ext if ext.startswith(".") else f".{ext}") for ext in file_exts
            ]
            return file_exts
