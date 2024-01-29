from blob import Client
from config import logger, settings
from transformer import Agent
from utils import create_inserter_objects


def main():
    logger.info("Initializing Blob Client")
    client = Client(
        file_exts=settings.FILE_EXTS,
        account_name=settings.BLOB_STORAGE_ACCOUNT_NAME,
        account_key=settings.BLOB_STORAGE_ACCOUNT_KEY,
        container_name=settings.BLOB_STORAGE_CONTAINER_NAME,
    )
    files = client.fetch()
    logger.info("Transforming Data")
    df_transformed = Agent(files).transform()
    logger.info("Preparing Database Inserter")
    inserter = create_inserter_objects(
        server=settings.MSSQL_SERVER,
        database=settings.MSSQL_DATABASE,
        username=settings.MSSQL_USERNAME,
        password=settings.MSSQL_PASSWORD,
    )
    logger.info(f"Inserting Data into {settings.OUTPUT_TABLE}")
    inserter.insert(df_transformed, settings.OUTPUT_TABLE)
    logger.info("Application completed successfully")
    return


if __name__ == "__main__":
    main()
