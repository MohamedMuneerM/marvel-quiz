import csv
import os
import tempfile
import random
import math
from utils import fileutils
from utils import iterableutils

# add return type
def read_csv(filename: str, has_headers: bool = False):
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = None
        if has_headers == True:
            header = next(csv_reader, None)

        for row in csv_reader:
            yield header, row

def get_row_count(filename: str) -> int:
    with open(filename) as f:
        return sum(1 for line in f)

def shuffle_csv(filename: str, chunk_size: int = 10000) -> None:
    combined_temp_filename = tempfile.mktemp()
    row_count = get_row_count(filename)
    temp_file_count = math.ceil(row_count / chunk_size)
    temp_files = [tempfile.mktemp() for _ in range(temp_file_count)]

    with open(filename, "r") as infile:
        reader = csv.reader(infile)

        for chunk in iterableutils.batched(reader, chunk_size):
            chunk = list(chunk)
            random.shuffle(chunk)
            # this decides granularity of the shuffle, increase decrease the 'batched_chunk_size'
            # with processing time in mind
            # should this be hardcoded?
            batched_chunk_size = 10
            batched_chunk = list(iterableutils.batched(chunk, batched_chunk_size))

            for batch in batched_chunk:
                selected_temp_file = random.choice(temp_files)
                with open(selected_temp_file, "a", newline="") as temp_outputfile:
                    writer = csv.writer(temp_outputfile)
                    writer.writerows(batch)

    random.shuffle(temp_files)
    fileutils.combine_files_into_one(combined_temp_filename, temp_files)
    os.replace(combined_temp_filename, filename)
    print("Done")
