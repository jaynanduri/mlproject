from customCNNClassifier import logger
from customCNNClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline, STAGE_NAME_DI

try:
    logger.info(f">>>>> Stage - 01: {STAGE_NAME_DI} started <<<<<")
    dataIngestion = DataIngestionTrainingPipeline()
    dataIngestion.main()
    logger.info(f">>>>> Stage - 01: {STAGE_NAME_DI} completed <<<<<")
except Exception as e:
    logger.exception(e)
