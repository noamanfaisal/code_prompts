import os

CODE_PATH = "/home/noaman/code/muslimkids/code_prompts/code/apps/billing"
PROMPT_TEMPLATES_PATH = "/home/noaman/code/muslimkids/code_prompts/prompt_templates"
PROMPTS_PATH = "/home/noaman/code/muslimkids/code_prompts/prompt_templates"

# settings.py

import os

# Factory pattern for match conditions
MATCH_CONDITIONS = {
    "PYTHON_FILE": lambda file_path: file_path.endswith(".py"),
    "MODEL_OR_UTILS": lambda file_path: os.path.basename(file_path) in {"models.py", "utils.py"},
    "MODELS": lambda file_path: os.path.basename(file_path) in {"models.py"},
    # Add more conditions as needed
}

MARKERS = {
    "IMPORT": {
        "start": "#### TYPE:IMPORT####",
        "end": "#### END ##########",
        "prompt": "Refactor the import statements in this segment.",
    },
    "PYTHON_CLASS": {
        "start": "#### TYPE:PYTHON CLASS####",
        "end": "#### END ##########",
        "prompt": "Analyze and optimize the Python class in this segment.",
    },
    "DJANGO_MODEL": {
        "start": "#### TYPE:DJANGO MODEL####",
        "end": "#### END ##########",
        "prompt": "Convert this Django model to a REST API schema.",
    },
    "PYTHON_FUNCTIONS": {
        "start": "#### TYPE:PYTHON FUNCTIONS####",
        "end": "#### END ##########",
        "prompt": "Improve the logic in this Python function.",
    },
    "PYTHON_CLASS_METHODS": {
        "start": "#### TYPE:PYTHON CLASS METHODS####",
        "end": "#### END ##########",
        "prompt": "Refactor the methods in this Python class.",
    },
}


