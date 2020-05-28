"""
A custom module for better logging format
Source: https://medium.com/@galea/python-logging-example-with-color-formatting-file-handlers-6ee21d363184
"""

import logging
import colorlog

def init_logger(log_file_name) -> logging.Logger:
    """
    Parameters:
        log_file_name:
            type: str
            description: name of the log file.
            ex: if app is passed as arg then app.log file will be created.
    Returns:
        logger:
            type: Logger
    """
    log_format = (
        '%(asctime)s - '
        '%(levelname)s - '
        '%(message)s'
    )
    colorlog_format = (
        '%(log_color)s '
        f'{log_format}'
    )
    colorlog.basicConfig(format=colorlog_format)
    logger = logging.getLogger()

    # if testing_mode:
    #     logger.setLevel(logging.DEBUG)
    # else:
    #     logger.setLevel(logging.INFO)

    logger.setLevel(logging.DEBUG)

    # Output full log
    file_handle = logging.FileHandler(log_file_name + '.log', "w")
    file_handle.setLevel(logging.DEBUG)
    formatter = logging.Formatter(log_format)
    file_handle.setFormatter(formatter)
    logger.addHandler(file_handle)

    # # Output warning log
    # file_handle = logging.FileHandler(log_file_name + '.warning.log', "w")
    # file_handle.setLevel(logging.WARNING)
    # formatter = logging.Formatter(log_format)
    # file_handle.setFormatter(formatter)
    # logger.addHandler(file_handle)

    # # Output error log
    # file_handle = logging.FileHandler(log_file_name + '.error.log', "w")
    # file_handle.setLevel(logging.ERROR)
    # formatter = logging.Formatter(log_format)
    # file_handle.setFormatter(formatter)
    # logger.addHandler(file_handle)

    return logger

LOG = init_logger(log_file_name="whatever")

if __name__ == "__main__":
    """Main funtion"""

    LOG.debug("Hello World, debug message")
    LOG.info("Hello World, info message")
    LOG.warning("Hello World, warning message")
    LOG.error("Hello World, error message")