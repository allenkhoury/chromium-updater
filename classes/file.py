import time
import shutil
import urllib.request
import zipfile
import os
from gettext import gettext as _
from classes import settings


def open_file(path: str) -> str:
    """
        Open and return file content

    :param path: str - file full path
    :return: str - file content
    """
    try:
        with urllib.request.urlopen(path) as file:
            return file.read().decode()
    except FileNotFoundError:
        print(_("File not found"))


def download_file(full_url: str, tries: int = 0) -> bool:
    file_name = settings.get('local_file')

    # Try downloading
    # If, for any reason, the download is interrupted, retry after 5 minutes
    # Maximum 5 tries, we don't want to spam the server if there are any errors

    try:
        with urllib.request.urlopen(full_url) as response, open(file_name, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
    except BaseException as exception:
        if tries == 5:
            # TODO: logging
            print('Download failed')
        else:
            time.sleep(300)
            download_file(full_url, tries + 1)

    return True


def install_file(tries: int = 0) -> bool:
    file_name = settings.get('local_file')
    install_path = settings.get('install_path')

    try:
        with zipfile.ZipFile(file_name, 'r') as zip_ref:
            zip_ref.extractall(install_path)
    except BaseException as exception:
        if tries == 5:
            # TODO: logging
            print('Extract failed')
        else:
            time.sleep(300)
            install_file(tries + 1)
    finally:
        if os.path.exists(file_name):
            os.remove(file_name)

    return True
