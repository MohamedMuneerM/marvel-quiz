import shutil

# add types
def combine_files_into_one(combine_file_name, filenames) -> None:
    with open(combine_file_name,'w') as combined_temp_file:
            for file in filenames:
                with open(file,'r') as file_stream:
                    shutil.copyfileobj(file_stream, combined_temp_file)