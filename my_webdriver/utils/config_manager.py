import json
import pathlib


class ConfigManager:
    ''' Класс створено для доступу до конфігураційних та тестових даних.
    Знаходяться вони у корневому каталозі у файлах config.json та auth_data.json '''

    @staticmethod
    def get_driver_conf():
        with open(pathlib.Path(__file__).parent.parent.parent.joinpath('config.json'), 'r', encoding='utf-8') as conf:
            browser_config = {k: v.lower().strip() if isinstance(v, str) else v for k, v in json.load(conf).items()}

        return browser_config

    @staticmethod
    def get_test_data(file_name):
        with open(pathlib.Path(__file__).parent.parent.parent.joinpath(f'test_data/{file_name}'), 'r', encoding='utf-8') as data:
            test_data = {k: v.strip() if isinstance(v, str) else v for k, v in json.load(data).items()}

        return test_data

    @staticmethod
    def get_url():
        with open(pathlib.Path(__file__).parent.parent.parent.joinpath('config.json'), 'r', encoding='utf-8') as conf:
            browser_config = {k: v.strip() if isinstance(v, str) else v for k, v in json.load(conf).items()}
        username = browser_config['username']
        password = browser_config['password']
        url = browser_config['url']

        return f'https://{username}:{password}@{url}'

