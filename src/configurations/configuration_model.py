import configparser
from pathlib import Path

class ConfigurationModel:
    def __init__(self):
        self.__welcome_text = None
        self.__sections = None
        self.load_configuration()

    def load_configuration(self):
        config_path = Path(__file__).parent.parent / 'settings.ini'

        if not Path.exists(config_path):
            raise Exception(f"Cannot resolve config file with the path {config_path}")
        config = configparser.ConfigParser()
        config.read(config_path)
        self.__sections = config.sections()
        self.__welcome_text = config.get("HomePage", "WelcomeText")

    @property
    def welcome_text(self):
        return self.__welcome_text

    @property
    def sections(self):
        return self.__sections
