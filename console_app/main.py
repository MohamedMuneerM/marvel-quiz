from utils import csvutils
from configurations.configuration_model import ConfigurationModel

configurations = ConfigurationModel()

def home_page():
    # add to config
    print("------------------------------")
    print(configurations.welcome_text)

def prep_env_and_get_questions() -> dict:
    question_limit = 20
    current_count = 0
    filepath = "src/data/marvel.csv"
    csvutils.shuffle_csv(filepath)
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
    print("Inside Main File")
    prep_env_and_get_questions()
    home_page()

if __name__ == "__main__":
    # testing code
    ...