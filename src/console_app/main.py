from utils import csvutils

def test():
    print("Inside Main File")
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
    
    print(questions_with_answers)

if __name__ == "__main__":
    # testing code
    ...