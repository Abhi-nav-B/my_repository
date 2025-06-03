import time
import logging

from types import NoneType
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta


logger = logging.getLogger('my_logger')


def duration(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        func_return = func(*args, **kwargs)
        logger.info(f'{"":=<80}')
        logger.info(f'Time took to execute: {time.strftime("%H:%M:%S", time.gmtime(time.time() - t1))}')
        print(f'Time took to execute: {time.strftime("%H:%M:%S", time.gmtime(time.time() - t1))}')
        logger.info(f'{"":=<80}')
        return func_return

    return wrapper


def get_exec_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        func_ret = func(*args, **kwargs)
        logger.info(f'{"":=<80}')
        logger.info(f'Time took to execute: {time.strftime("%H:%M:%S", time.gmtime(time.time() - t1))}')
        logger.info(f'{"":=<80}')
        return func_ret
    return wrapper


def countdown(t, msg: str | None = None, is_msg: bool = True):
    time.sleep(0.5)  # helps to remove inline log in countdown representation

    base = t
    t = int(t)

    if is_msg:
        if msg is not None:
            print(msg)
        else:
            print(f'Waiting for {t // 60:02d} minutes {t % 60:02d} seconds')

    while t >= 0:
        minutes = t // 60
        seconds = t % 60
        timer = '{:02d}:{:02d}'.format(minutes, seconds)
        # print(f'\r{timer} |{'═' * (100-int((t / base) * 100)):100}|', end="")  # overwrite previous line
        print(f'\r{timer} │{'░' * (100-int((t / base) * 100)):100}│ {(100-(t / base) * 100):.2f}%', end="")  # overwrite previous line
        # print(f'\r{timer} │{'▒' * (100-int((t / base) * 100)):100}│ {(100-(t / base) * 100):.2f}%', end="")  # overwrite previous line
        # print(f'\r{timer} │{'█' * (100-int((t / base) * 100)):100}│ {(100-(t / base) * 100):.2f}%', end="")  # overwrite previous line
        time.sleep(1)
        t -= 1
    print('')


def date_range(from_date: tuple, to_date: tuple, step = 1):
    """
    returns date from date range in the given step
    :param from_date: (year, month, day)
    :param to_date:  (year, month, day)
    :param step: default is 1
    :return: date
    """

    if not isinstance(step, int):
        raise ValueError('"step" must be a integer.')

    if step >=0 and from_date > to_date:
        raise ValueError(f'"from_date" should be smaller than the "to_date".')

    if step < 0 and from_date < to_date:
        raise ValueError('"from_date" should be greater than the "to_date".')

    from_date = date(*from_date)
    to_date = date(*to_date)

    if step>=0:
        while from_date < to_date:
            yield from_date
            from_date = from_date + timedelta(days=step)
    else:
        while from_date > to_date:
            yield from_date
            from_date = from_date + timedelta(days=step)


def show_in_box(list_of_data:list, box_length = 30, enable_logs = False, double_line = False):
    if double_line:
        if enable_logs:
            logger.info('╔' + f'{'':═^{box_length}}' + '╗')
            for element in list_of_data:
                if type(element) is list:
                    element = ' '.join(element)
                logger.info('║ ' + f'{element:<{box_length - 2}}' + ' ║')
            logger.info('╚' + f'{'':═^{box_length}}' + '╝')

        if not enable_logs:
            print('╔' + f'{'':═^{box_length}}' + '╗')
            for element in list_of_data:
                if type(element) is list:
                    element = ' '.join(element)
                print('║ ' + f'{element:<{box_length - 2}}' + ' ║')
            print('╚' + f'{'':═^{box_length}}' + '╝')

    if not double_line:
        if enable_logs:
            logger.info('┌' + f'{'':─^{box_length}}' + '┐')
            for element in list_of_data:
                if type(element) is list:
                    element = ' '.join(element)
                logger.info('│ ' + f'{element:<{box_length - 2}}' + ' │')
            logger.info('└' + f'{'':─^{box_length}}' + '┘')

        if not enable_logs:
            print('┌' + f'{'':─^{box_length}}' + '┐')
            for element in list_of_data:
                if type(element) is list:
                    element = ' '.join(element)
                print('│ ' + f'{element:<{box_length - 2}}' + ' │')
            print('└' + f'{'':─^{box_length}}' + '┘')


def get_week_start_end_date(yyyy, mm, dd):
    """
    :param yyyy: year, in yyyy format, i.e. 2025
    :param mm: month, range from 1 to 12
    :param dd: day, range from 1 to 31
    :return:
    """

    if not 0 < mm < 13:
       raise ValueError('month must be in 1..12')

    d_start, d_end = get_month_start_end_day(mm, yyyy)
    if not d_start <= dd <= d_end:
        raise ValueError(f'date must be in {d_start}..{d_end}')

    dt = date(yyyy, mm, dd)
    start = dt - timedelta(days=dt.weekday())
    end = start + timedelta(days=6)
    start = start
    return start, end


def get_month_start_end_day(mm: int, yyyy: int = None):
    """
    get the start and end day of the given month.\n
    the year must be provided to get the correct end day of February month of a leap year if the current year is not the one, and vice versa.
    :param mm: month number, range from 1 to 12
    :param yyyy: year, in yyyy format, i.e. 2025, if not provided, the current year will be considered.
    :return: start and end day of a given month
    """

    if not 0 < mm < 13:
       raise ValueError('month must be in 1..12')

    if yyyy is None:
        yyyy = datetime.now()
    else:
        yyyy = date(yyyy, mm, 1)

    # Start of the month
    start_date = datetime(yyyy.year, mm, 1)
    # End of the month
    if mm == 12:
        end_date = datetime(yyyy.year, mm, 31)
    else:
        end_date = datetime(yyyy.year, mm + 1, 1) - timedelta(days=1)

    return start_date.day, end_date.day


def seconds_since_epoch(yyyy: int, mm: int, dd: int,
                        HH: int | None = None, MM: int | None = None, ss: int | None = None,
                        epoch_year: int = 1970, time_zone: int | None = None) -> int:
    """

    :param yyyy: year, in yyyy format, i.e. 2025
    :param mm: month, range from 1 to 12
    :param dd: day, range from 1 to 31
    :param HH: hour, range from 0 to 23
    :param MM: minute, range from 0 to 59
    :param ss: second, range from 0 to 59
    :param epoch_year: starting year, from which the time will be calculated. default is 1970
    :param time_zone: if the input time is not in utc, provide the timezone in seconds to convert in utc, i.e. India = 19800, Greenland = -7200. DST is not considered in calculation.
    :return: seconds since the epoch
    """
    if not 0 < mm < 13:
        raise ValueError('month must be in 1..12')

    d_start, d_end = get_month_start_end_day(mm, yyyy)
    if not d_start <= dd <= d_end:
        raise ValueError(f'date must be in {d_start}..{d_end}')

    if not 0 <= HH <= 23:
        raise ValueError('hours must be in 1..24')

    if not 0 <= MM <= 59:
        raise ValueError('minutes must be in 0..59')

    if not 0 <= ss <= 59:
        raise ValueError('seconds must be in 0..59')

    if not isinstance(time_zone, (NoneType, int)):
        raise ValueError('time zone either can be "None" or a valid integer')

    if time_zone is None:
        time_zone = 0

    dt = datetime(yyyy, mm, dd, HH, MM, ss)

    duration_in_seconds = int((dt - datetime(epoch_year, 1, 1) - timedelta(seconds=time_zone)).total_seconds())
    return duration_in_seconds


def seconds_to_timestamp(seconds: int, epoch_year: int = 1970, time_zone: int|None = None) -> datetime:
    """
    converts seconds to timestamp.
    :param seconds: seconds since epoch
    :param epoch_year: starting year, from which the time will be calculated. default is 1970
    :param time_zone: if the input time is in utc, provide the timezone in seconds to convert in local time, i.e. India = 19800, Greenland = -7200. DST is not considered in calculation.
    :return:
    """

    if not isinstance(seconds, int):
        raise ValueError('input value must be an integer')

    if not isinstance(time_zone, (NoneType, int)):
        raise ValueError('time zone either can be "None" or a valid integer')

    if time_zone is None:
        time_zone = 0

    return (datetime.fromtimestamp(seconds)
            - timedelta(seconds=time.localtime().tm_gmtoff)
            + timedelta(seconds=time_zone)
            + relativedelta(years=(epoch_year - 1970)))


if __name__ == '__main__':
    print('Starting Countdown...')
    countdown(17)
    print('Countdown End')