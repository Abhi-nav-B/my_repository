import os
import logging
from datetime import datetime

logger = logging.getLogger('my_logger')


class CustomFormatter(logging.Formatter):

    # Define ANSI escape codes for text colors
    # RED = '\033[29m'
    RED = '\033[38;2;255;0;0m'
    # PINK = '\033[31m'
    PINK = '\033[38;2;255;0;100m'
    GREEN = '\033[32m'
    # YELLOW = '\033[33m'
    YELLOW = '\033[38;2;200;200;0m'
    # BLUE = '\033[34m'
    BLUE = '\033[38;2;0;150;255m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    RESET = '\033[0m'  # Reset to default color

    # create formatter and add it to the handlers
    formatter = '{asctime} | {filename:23} | Line {lineno:4} | {levelname:8} | {message}'

    FORMATS = {
        logging.DEBUG: BLUE + formatter + RESET,
        logging.INFO: GREEN + formatter + RESET,
        logging.WARNING: YELLOW + formatter + RESET,
        logging.ERROR: PINK + formatter + RESET,
        logging.CRITICAL: RED + formatter + RESET
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, style='{')
        return formatter.format(record)


def start_logger(logger_path: str = None, file_log_level=logging.INFO, console_log_level=logging.INFO):
    # initialising logger
    lgr = logging.getLogger('my_logger')

    # changing the default logging level to debug from warning
    lgr.setLevel(logging.DEBUG)

    if logger_path is not None:
        if logger_path[logger_path.find('.', 1):].lower() in ['.txt', '.log']:
            filename = logger_path
        else:
            default_file_name = f'{datetime.now().strftime("%Y-%m-%d")}.log'
            filename = os.path.join(logger_path, default_file_name)

        # create file handler that logs info and higher level messages
        file_handler = logging.FileHandler(filename, encoding='utf-8')
        file_handler.setLevel(file_log_level)

        # create formatter and add it to the handlers
        formatter = logging.Formatter(
            fmt='{asctime} | {filename:23} | Line {lineno:4} | {levelname:8} | {message}',
            style='{')

        file_handler.setFormatter(formatter)

        # add the handlers to logger
        lgr.addHandler(file_handler)

    # create console handler that logs info and higher level messages
    console_handler = logging.StreamHandler()
    console_handler.setLevel(console_log_level)

    console_handler.setFormatter(CustomFormatter())

    # add the handlers to logger
    lgr.addHandler(console_handler)


if __name__ == '__main__':
    # start_logger('my_test_logger.log', console_log_level=logging.DEBUG)
    start_logger(console_log_level=logging.DEBUG)

    logger = logging.getLogger('my_logger')

    logger.debug('this is debug data')
    logger.info('this is an information')
    logger.warning('this is a warning')
    logger.error('this is an error')
    logger.critical('this is a critical error')
