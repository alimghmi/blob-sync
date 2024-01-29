from decouple import config

FILE_EXTS = config("FILE_EXTS", default="*").replace(" ", "").split(",")
LOG_LEVEL = config("LOG_LEVEL", default="INFO")
OUTPUT_TABLE = config("OUTPUT_TABLE")
INSERTER_MAX_RETRIES = config("INSERTER_MAX_RETRIES", default=3, cast=int)
MSSQL_SERVER = config("MSSQL_SERVER")
MSSQL_DATABASE = config("MSSQL_DATABASE")
MSSQL_USERNAME = config("MSSQL_USERNAME")
MSSQL_PASSWORD = config("MSSQL_PASSWORD")
BLOB_STORAGE_ACCOUNT_NAME = config("BLOB_STORAGE_ACCOUNT_NAME")
BLOB_STORAGE_ACCOUNT_KEY = config("BLOB_STORAGE_ACCOUNT_KEY")
BLOB_STORAGE_CONTAINER_NAME = config("BLOB_STORAGE_CONTAINER_NAME")
