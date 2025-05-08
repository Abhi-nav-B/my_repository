import os
import logging
from datetime import datetime

logger = logging.getLogger('my_logger')


def start_logger(logger_path: str, file_log_level=logging.INFO, console_log_level=logging.INFO):
    if logger_path[logger_path.find('.', 1):].lower() in ['.txt', '.log']:
        filename = logger_path
    else:
        default_file_name = f'{datetime.now().strftime("%Y-%m-%d")}.log'
        filename = os.path.join(logger_path, default_file_name)

    lgr = logging.getLogger('my_logger')
    lgr.setLevel(logging.DEBUG)

    # create file handler that logs info and higher level messages
    file_handler = logging.FileHandler(filename, encoding='utf-8')
    file_handler.setLevel(file_log_level)

    # create console handler that logs info and higher level messages
    console_handler = logging.StreamHandler()
    console_handler.setLevel(console_log_level)

    # create formatter and add it to the handlers
    formatter = logging.Formatter(
        fmt='{asctime} | {filename:23} | Line {lineno:4} | {levelname:8} | {message}',
        style='{')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # add the handlers to logger
    lgr.addHandler(console_handler)
    lgr.addHandler(file_handler)

    # time.sleep(2)
    return None
