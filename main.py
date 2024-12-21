from settings import MATCH_CONDITIONS, CODE_PATH
from file_browser import browse_files
from file_marker import extract_code_segments

class Main:

    def __init__(self):
        pass

    def create_prompt(self, matching_condition):
        # matching condition function
        matching_condition_function = MATCH_CONDITIONS[matching_condition]
        # calling file_browsing
        files = browse_files(CODE_PATH, matching_condition_function)
        for file in files:
            for file_path, marker_name, code_segment in extract_code_segments(file):
                print(file_path)
                print(marker_name)
                print('############################################')
                print(code_segment)
                print('############################################')

main = Main()

main.create_prompt('MODELS')