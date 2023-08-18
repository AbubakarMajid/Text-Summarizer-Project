from TextSummarizer.pipeline.stage01 import dataIngestionTrainingPipeline
from TextSummarizer.pipeline.stage02 import dataValidationTrainingPipeline
from TextSummarizer.pipeline.stage03 import dataTransformationTrainingPipeline
from TextSummarizer.pipeline.stage04 import ModelTrainerPipeline
from TextSummarizer.pipeline.stage05 import ModelEvaluationPipeline
from TextSummarizer.logging import logger

STAGE_NAME = "data ingestion stage"

try:
    logger.info(f">>>>> Stage {STAGE_NAME} started >>>>>>")
    data_ingestion = dataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"<<<<<<<< stage {STAGE_NAME} completed >>>>>>>")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "data validation stage"

try:
    logger.info(f">>>>> Stage {STAGE_NAME} started >>>>>>")
    data_validation = dataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f"<<<<<<<< stage {STAGE_NAME} completed >>>>>>>")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "data transformation stage"

try:
    logger.info(f">>>>> Stage {STAGE_NAME} started >>>>>>")
    data_transformation = dataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f"<<<<<<<< stage {STAGE_NAME} completed >>>>>>>")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Trainer stage"

try:
    logger.info(f">>>>> Stage {STAGE_NAME} started >>>>>>")
    model_trainer = ModelTrainerPipeline()
    model_trainer.main()
    logger.info(f"<<<<<<<< stage {STAGE_NAME} completed >>>>>>>")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation stage"

try:
    logger.info(f">>>>> Stage {STAGE_NAME} started >>>>>>")
    model_trainer = ModelTrainerPipeline()
    model_trainer.main()
    logger.info(f"<<<<<<<< stage {STAGE_NAME} completed >>>>>>>")

except Exception as e:
    logger.exception(e)
    raise e