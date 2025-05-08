import sys
import requests
import wget
import zipfile
import os

from logs.exception_logs import exception_log

DRIVER_PATH = r'.\browser'


# def write_in_file(issue, in_detail):
#     with open(CURRENT_WORKING_DIR + '\\error_log.txt', 'w') as f:
#         f.writelines(issue)
#         f.writelines(in_detail)


# def exception_log(e):
#     exc_type, exc_obj, exc_tb = sys.exc_info()
#     f_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
#     print((exc_type, f_name, f'Line: {exc_tb.tb_lineno}'))
#     print(e)
#     write_in_file(str((exc_type, f_name, f'Line: {exc_tb.tb_lineno}')), '\n' + str(e))


def update_chromedriver():
    try:
        # get the latest chrome driver version number
        url = 'https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions.json'
        response = requests.get(url)
        version_number = eval(response.text)
        version_number = version_number['channels']['Stable']['version']

        # build the download url
        download_url = (f'https://storage.googleapis.com/chrome-for-testing-public/{version_number}'
                        f'/win64/chromedriver-win64.zip')

        # download the zip file using the url built above
        # latest_driver_zip = wget.download(download_url, 'chromedriver.zip')
        latest_driver_zip = wget.download(download_url)

        # extract the zip file
        with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
            zip_ref.extractall(DRIVER_PATH)  # you can specify the destination folder path here
        # delete the zip file downloaded above
        os.remove(latest_driver_zip)

    except requests.exceptions.ConnectTimeout:
        e = (f'Connection Timeout!, unable to download the "chromedriver.exe",'
             f'\ncheck if path "https://googlechromelabs.github.io/chrome-for-testing/" is accessible.')
        exception_log(e)
        return -1

    except Exception as e:
        exception_log(e)
        sys.exit()
