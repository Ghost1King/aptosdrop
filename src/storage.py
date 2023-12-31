from src.file_manager import FileManager
from src.paths import (TempFiles,
                       APP_CONFIG_FILE)
from src.schemas.app_config import AppConfigSchema


class Storage:
    __instance = None

    class __Singleton:
        DEFAULT_RPC_URL = '"https://rpc.ankr.com/http/aptos/v1"'

        def __init__(self):
            self.__wallets_data = FileManager().get_wallets_from_files()
            self.__shuffle_wallets = False
            self.__app_config = self.__load_app_config()
            self.__wallet_balances = []

        def set_wallets_data(self, value):
            self.__wallets_data = value

        def set_shuffle_wallets(self, value):
            self.__shuffle_wallets = value

        def get_wallets_data(self):
            return self.__wallets_data

        def get_shuffle_wallets(self):
            return self.__shuffle_wallets

        def get_app_config(self) -> AppConfigSchema:
            return self.__app_config

        def __load_app_config(self):
            try:
                config_file_data = FileManager().read_data_from_json_file(APP_CONFIG_FILE)
                return AppConfigSchema(**config_file_data)
            except Exception as e:
                raise e

        def append_wallet_balance(self, value):
            self.__wallet_balances.append(value)

        def get_wallet_balances(self):
            return self.__wallet_balances

        def reset_wallet_balances(self):
            self.__wallet_balances = []

        def update_app_config(self, config: AppConfigSchema):
            self.__app_config = config

    def __new__(cls):
        if not Storage.__instance:
            Storage.__instance = Storage.__Singleton()
        return Storage.__instance

