import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchDriverException, SessionNotCreatedException
from browser.chromedriver_manager import update_chromedriver
from logs.exception_logs import exception_log


DRIVER_PATH = r'.\browser\chromedriver-win64\chromedriver.exe'


# def exception_log(e):
#     exc_type, exc_obj, exc_tb = sys.exc_info()
#     f_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
#     print((exc_type, f_name, f'Line: {exc_tb.tb_lineno}'))
#     print(e)


def launch_browser(url: str = None,
                   *, browser_path = None,
                   is_headless: bool = False,
                   is_incognito: bool = False) -> webdriver.Chrome|int:

    if browser_path is None:
        browser_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

    if not os.path.isfile(browser_path):
        raise FileNotFoundError(f'The path, "{browser_path}" is incorrect, provide the correct path.')

    options = webdriver.ChromeOptions()
    options.binary_location = browser_path
    options.add_argument('--start-maximized')
    options.add_argument('--log-level=3')
    options.add_argument('–-disable-notifications')

    if is_incognito:
        options.add_argument('--incognito')

    if is_headless:
        options.add_argument('--headless')

    if not os.path.isfile(DRIVER_PATH):
        raise FileNotFoundError(f'The path, "{DRIVER_PATH}" is incorrect, provide the correct path.')

    service = Service(DRIVER_PATH)

    try:
        chrome = webdriver.Chrome(service=service, options=options)

        if is_headless:
            chrome.set_window_size(7680, 4320)

        if url is not None:
            chrome.get(url)

        return chrome

    except NoSuchDriverException:
        print('"chromedriver.exe" is being downloaded, please wait!')
        status = update_chromedriver()

        if status == -1:
            return -1

        print('\n"chromedriver.exe" has been downloaded, re-execute the script.')
        print('If the "chromedriver.exe" is being downloaded everytime the script is executed then update your browser.')
        return -1

    except SessionNotCreatedException:
        print('"chromedriver.exe" is being updated, please wait!')
        status = update_chromedriver()
        if status == -1: return -1

        print('\n"chromedriver.exe" has been updated, re-execute the script.')
        print('If the "chromedriver.exe" is being downloaded everytime the script is executed then update your browser.')
        return -1

    except Exception as e:
        exception_log(e)
        return -1
