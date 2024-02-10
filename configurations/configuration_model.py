import configparser
from pathlib import Path

class ConfigurationModel:
    def __init__(self):
        self.__welcome_text = None
        self.__sections = None
        self.__questions_with_options_file_path = None
        self.__number_of_questions_per_game = None
        self.load_configuration()

    def load_configuration(self):
        config_path = Path(__file__).parent.parent / 'settings.ini'

        if not Path.exists(config_path):
            raise Exception(f"Cannot resolve config file with the path {config_path}")
        config = configparser.ConfigParser()
        config.read(config_path)
        self.__sections = config.sections()
        self.__welcome_text = config.get("HomePage", "WelcomeText")
        self.__questions_with_options_file_path = config.get("AppSettings", "QuestionsWithOptionsFilePath")
        self.__number_of_questions_per_game = config.get("AppSettings", "NumberOfQuestionsPerGame")

        if not self.__number_of_questions_per_game.isnumeric():
            raise ValueError("number_of_questions_per_game value in configuration must of a valid integer type")
        
        self.__number_of_questions_per_game = int(self.__number_of_questions_per_game)

    @property
    def number_of_questions_per_game(self):
        return self.__number_of_questions_per_game

    @property
    def questions_with_options_file_path(self):
        return self.__questions_with_options_file_path

    @property
    def welcome_text(self):
        return self.__welcome_text

    @property
    def sections(self):
        return self.__sections
