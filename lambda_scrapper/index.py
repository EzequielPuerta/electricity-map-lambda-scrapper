from loguru import logger


def handler(event, context):
    logger.info(event)
