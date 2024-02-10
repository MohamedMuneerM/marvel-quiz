from utils import csvutils, consoleutils
from configurations.configuration_model import ConfigurationModel

configurations = ConfigurationModel()

def home_page():
    print("------------------------------")
    print(configurations.welcome_text)

def prep_env(filepath: str) -> None:
    csvutils.shuffle_csv(filepath)

def get_questions(filepath: str) -> dict:
    question_limit = 20
    current_count = 0
    questions_with_answers = dict()
    for header, record in csvutils.read_csv(filepath, False):
        print(record)
        if record == None:
            raise Exception(f"Unexpected error when loading the csv file...")

        if len(record) != 5:
            raise Exception(f"Columns Mismatch. Expected columns 5, Actual columns in the file {len(record)}")
        
        if current_count > question_limit:
            break

        questions_with_answers[record[0]] = record[1:]

        current_count+=1
    
    return questions_with_answers

def test():
    try:
        print(f"Inside Main File {__file__}")
        filepath = configurations.questions_with_options_file_path
        prep_env(filepath)
        get_questions(filepath)
        home_page()
        print(consoleutils.get_user_input("hey there", input_type=int))

    except Exception as error:
        print(error)

if __name__ == "__main__":
    # testing code
    ...