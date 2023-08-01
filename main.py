from TextSummarizer.pipeline.stage01 import dataIngestionTrainingPipeline
from TextSummarizer.pipeline.stage02 import dataValidationTrainingPipeline
from TextSummarizer.logging import logger

STAGE_NAME = "data ingestion stage"

try:
    logger.info(">>>>> Stage {ST\AGE_NAME} started >>>>>>")
    data_ingestion = dataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info("<<<<<<<< stage {STAGE_NAME} completed >>>>>>>")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "data validation stage"

try:
    logger.info(">>>>> Stage {STAGE_NAME} started >>>>>>")
    data_validation = dataValidationTrainingPipeline()
    data_validation.main()
    logger.info("<<<<<<<< stage {STAGE_NAME} completed >>>>>>>")

except Exception as e:
    logger.exception(e)
    raise e

