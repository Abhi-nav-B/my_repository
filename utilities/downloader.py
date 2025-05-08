import os
import wget
import shutil
import zipfile
import requests

from logs.exception_logs import exception_log


def download_from_url(url: str, output_dir_name: str | None = None) -> bool:
    """
    It downloads the file from the given file download link.

    :param url: download link of a file.
    :param output_dir_name: Zip files are automatically extracted at given directory. \
    If directory name is not given then the directory name remain same as the zip file name.
    :return: True on successful download else False
    """
    try:
        # download the zip file using the url built above
        latest_download = wget.download(url)

        #checking for zip file
        if latest_download.split('.')[-1] in ['zip']:
            # extract the zip file
            with zipfile.ZipFile(latest_download, 'r') as zip_ref:
                zip_ref.extractall(output_dir_name)  # you can specify the destination folder path here

            # delete the zip file downloaded above
            os.remove(latest_download)

            # moving extracted files and folders to parent folder
            if output_dir_name is not None:
                move_files_folders(rf'{output_dir_name}\{latest_download.split('.')[0]}', output_dir_name)

        return True

    except requests.exceptions.ConnectTimeout:
        e = f'Connection Timeout!, unable to download file from the link:\n{url}'
        exception_log(e)
        return False

    except Exception as e:
        exception_log(e)
        return False


def move_files_folders(source_dir, target_dir) -> str | None:
    """
    move files and folders from one directory to another directory.
    the source directory is deleted after moving files and folders to the target directory.
    :param source_dir:
    :param target_dir:
    :return: returns target directory path on success else None
    """
    try:
        file_names = os.listdir(source_dir)

        for file_name in file_names:
            shutil.move(os.path.join(source_dir, file_name), target_dir)

        os.removedirs(source_dir)

        return target_dir

    except Exception as e:
        exception_log(e)
        return None