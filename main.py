
# # checking browser
# if __name__ == '__main__':
#     import sys
#     from browser.browser import launch_browser
#
#     driver = launch_browser('https://navbharattimes.com')
#     if driver == -1:
#         sys.exit()
#     print(driver.title)
#     driver.quit()


# # checking exception logs
# if __name__ == '__main__':
#     from logs.exception_logs import exception_log
#     try:
#         a = 0
#         b = 1
#         c = b/a
#     except Exception as e:
#         exception_log(e, True)


# # checking logger
# if __name__ == '__main__':
#     from logs.logger_setup import start_logger
#     from logs.exception_logs import exception_log
#
#     start_logger('.')
#     try:
#         a = 0
#         b = 1
#         c = b/a
#     except Exception as e:
#         exception_log(e, True)

# checking common functions
if __name__ == '__main__':
    from logs.logger_setup import start_logger
    from utilities import common_function as cm

    start_logger('.')
    cm.show_in_box(['This is a sample text', 'This is another sample text'], double_line=True, enable_logs=True)

    dates = cm.date_range((2025, 2, 1), (2025, 3, 31), 3)
    for date in dates:
        print(date)

    print(cm.get_month_start_end_day(2, 2024))

    print(cm.get_week_start_end_date(2024, 2, 29))

    import datetime
    dt = datetime.datetime.now()
    secs = cm.seconds_since_epoch(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
    print(secs)
    print(cm.seconds_to_timestamp(secs, time_zone=19800))
