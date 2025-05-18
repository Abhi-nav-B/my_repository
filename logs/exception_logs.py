import os
import sys
import logging

logger = logging.getLogger('my_logger')


def write_in_file(issue, in_detail, file_path):
    with open(rf'{file_path}\error_log.txt', 'w') as f:
        f.writelines(issue)
        f.writelines(in_detail)


def exception_log(e, is_file = False, file_path = '.'):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    f_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]

    logger.error((exc_type, f_name, f'Line: {exc_tb.tb_lineno}'))
    logger.error(e)
    # print((exc_type, f_name, f'Line: {exc_tb.tb_lineno}'))
    # print(e)

    if is_file:
        write_in_file(str((exc_type, f_name, f'Line: {exc_tb.tb_lineno}')), '\n' + str(e), file_path)
