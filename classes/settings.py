import json


def get(config_name: str, default: str = "") -> str:
    try:
        with open('json/config.json', encoding="utf-8") as json_file:
            json_data = json.load(json_file)

        if config_name in json_data:
            return json_data[config_name]

    except BaseException as exception:
        print('Failed to read from json data.')

    return default
