from TextSummarizer.pipeline.stage01 import dataIngestionTrainingPipeline
from TextSummarizer.logging import logger

STAGE_NAME = "data Ingestion stage"

try:
    logger.info(">>>>> Stage {STAGE_NAME} started >>>>>>")
    data_ingestion = dataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info("<<<<<<<< stage {STAGE_NAME} completed >>>>>>>")

except Exception as e:
    logger.exception(e)
    raise e