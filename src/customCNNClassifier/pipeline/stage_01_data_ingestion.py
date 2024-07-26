from customCNNClassifier.components.data_ingestion import DataIngestion
from customCNNClassifier.config.configuration import ConfigurationManager
from customCNNClassifier import logger

STAGE_NAME_DI = "Data Ingestion"


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    @staticmethod
    def main():
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.unzip_zip_file()
        except Exception as e:
            raise e


if __name__ == "__main__":
    try:
        logger.info(f">>>>> Stage - 01: {STAGE_NAME_DI} started <<<<<")
        dataIngestion = DataIngestionTrainingPipeline()
        dataIngestion.main()
        logger.info(f">>>>> Stage - 01: {STAGE_NAME_DI} completed <<<<<")
    except Exception as e:
        logger.exception(e)
