import datetime

import numpy as np
import pandas as pd

from config import logger


class Agent:
    def __init__(self, files: list) -> None:
        self.files = files
        self.dataframe = None
        self.files_per_isin = {}

    def transform(self) -> pd.DataFrame:
        logger.info("Starting data transformation.")
        self.parse_files()
        self.init_df()
        self.add_timestamp()
        logger.info("Data transformation completed successfully.")
        logger.debug(f"\n{self.dataframe}")
        return self.dataframe

    def parse_files(self) -> None:
        try:
            for path in self.files:
                isin, folder = self.extract_isin_and_folder(path)
                if isin not in self.files_per_isin:
                    self.files_per_isin[isin] = {}

                self.files_per_isin[isin][folder] = path
            logger.debug("File parsing completed.")
        except Exception as e:
            logger.error(f"Failed to parse the files list. Error: {e}")
            raise

    def init_df(self) -> None:
        try:
            logger.debug("Initializing DataFrame from parsed data.")
            self.dataframe = pd.DataFrame(self.files_per_isin).transpose()
            self.dataframe.reset_index(inplace=True)
            self.dataframe.rename(columns={"index": "ISIN"}, inplace=True)
            self.dataframe.replace({np.nan: None}, inplace=True)
            logger.debug("DataFrame initialized successfully.")
        except Exception as e:
            logger.error(f"Failed to init dataframe. Error: {e}")
            raise

    def add_timestamp(self) -> None:
        try:
            logger.debug("Adding timestamp to DataFrame.")
            self.dataframe["timestamp_created_utc"] = datetime.datetime.utcnow()
            logger.debug("Timestamp added successfully.")
        except Exception as e:
            logger.error(f"Failed to add timestamps. Error: {e}")
            raise

    @staticmethod
    def extract_isin_and_folder(path):
        folder, file = path.split("/")
        isin = file.split("_")[-1].split(".")[0]
        return isin, folder
