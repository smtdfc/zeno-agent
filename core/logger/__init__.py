from loguru import logger

def setup_logger():
    logger.add("file_{time}.log", rotation="500 MB")