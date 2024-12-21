from settings import MATCH_CONDITIONS, CODE_PATH
from file_browser import browse_files
from file_marker import extract_code_segments
from prompt_creator import create_prompt
import uuid

class Main:

    def __init__(self):
        pass

    def create_prompt(self, matching_condition):
        # matching condition function
        matching_condition_function = MATCH_CONDITIONS[matching_condition]
        # calling file_browsing
        files = browse_files(CODE_PATH, matching_condition_function)
        for file in files:
            
            unique_id = str(uuid.uuid4())
            for counter, value_pack in enumerate(extract_code_segments(file)):
                file_path = value_pack[0]
                marker_name = value_pack[1]
                code_segment = value_pack[2]                
                print(file_path)
                print(marker_name)
                print('############################################')
                print(code_segment)
                print('############################################')
                create_prompt(counter, unique_id, marker_name, 
                  file_path, code_segment)

main = Main()
main.create_prompt('MODELS')