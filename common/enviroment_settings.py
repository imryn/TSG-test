import os
from dotenv import load_dotenv
from pathlib import Path

class EnvironmentSettings:

    def __init__(self):
        file_path = Path(f"{os.getcwd()}/.env")
        load_dotenv(override=True, dotenv_path=file_path)

    ''' reaturn each key exist in the .env file '''
    @staticmethod
    def get_env_variable(key_name):
        return os.getenv(key_name,"")

    ''' reaturn dictionary of the .env file '''
    def get_env_variable_dict(self):
        env_dict = {}
        for name in self.__store_env_keys_in_array():
            env_value = os.getenv(name)
            env_dict[name] = env_value
        return env_dict

    ''' for making sure the example env have every variable that exist in the env file '''
    @staticmethod
    def __store_env_keys_in_array():
        lines = []
        try:
            import sys
            file_path = Path(f"{os.getcwd()}/example.env")
            with open(file_path) as f:
                for line in f:
                    if not line.startswith('#'):
                        lines.append(line.strip())
            return lines

        except FileExistsError as e:
            print(e)
