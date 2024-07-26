import os

import zipfile
import gdown
from customCNNClassifier import logger
from customCNNClassifier.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config=DataIngestionConfig) -> None:
        self.config = config

    def download_file(self) -> None:
        """
        Fetch data from Data Source. Data source is a constant path set in config folder.
        """
        try:
            dataset_url = self.config.source_url
            zip_download_file = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            logger.info(f"Downloading data from {dataset_url} into file {zip_download_file}.")

            file_id = dataset_url.split("/")[-2]
            prefix = "https://drive.google.com/uc?/export=download&id="
            gdown.download(prefix + file_id, zip_download_file)
            logger.info(f"Downloaded data from {dataset_url} into file {zip_download_file}")
        except Exception as e:
            raise e

    def unzip_zip_file(self):
        """
        Extracts contents of the ZIP file into the directory.
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zipFile:
            zipFile.extractall(unzip_path)