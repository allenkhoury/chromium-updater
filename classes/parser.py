import time
from classes import settings
import urllib.parse


def get_latest_version_url() -> str:
    parameters = {
        'alt': 'media'
    }

    full_version = '/'.join([settings.get('os'), 'LAST_CHANGE'])
    full_version = urllib.parse.quote(full_version, safe='')

    full_url = settings.get('url') + full_version + '?' + urllib.parse.urlencode(parameters)
    return full_url


def get_update_url(version: str) -> str:
    full_version = get_full_version(version)
    parameters = {
        'alt': 'media'
    }

    full_url = settings.get('url') + full_version + '?' + urllib.parse.urlencode(parameters)
    return full_url


def get_full_version(version: str) -> str:
    full_version = '/'.join([settings.get('os'), version, settings.get('file')])
    return urllib.parse.quote(full_version, safe='')


def time_in_micro() -> int:
    return round(time.time() * 1000000)
