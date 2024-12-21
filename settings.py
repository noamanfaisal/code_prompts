import os

CODE_PATH = "/home/noaman/code/muslimkids/code_prompts/code/apps/billing"
PROMPT_TEMPLATES_PATH = "/home/noaman/code/muslimkids/code_prompts/prompt_templates"
PROMPTS_PATH = "/home/noaman/code/muslimkids/code_prompts/prompts"

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
        "prompt": "python37/django111/import.prompt",
        "name":"import"
    },
    "PYTHON": {
        "start": "#### TYPE:PYTHON CLASS####",
        "end": "#### END ##########",
        "prompt": "python37/django111/python.prompt",
        "name":"python"
    },
    "DJANGO_MODEL": {
        "start": "#### TYPE:DJANGO MODEL####",
        "end": "#### END ##########",
        "prompt": "python37/django111/model.prompt",
        "name":"model"
    },
}

def CREATE_FILE_NAME_AND_PROMPT_FILE(counter, unique_id, marker_name, source_file_name_with_path):
    """
    Creates a unique file name and prompt file name based on the source file, marker, and counter.

    Args:
        counter (int): Counter for the file.
        unique_id (str): A unique identifier for the file.
        marker_name (str): Marker name to identify the prompt.
        source_file_name_with_path (str): Full path of the source file.

    Returns:
        tuple: (prompt_file, file_name)
    """
    # Get the last directory in the path
    directory_name = os.path.basename(os.path.dirname(source_file_name_with_path))

    # Get the file name without extension
    file_name_without_ext = os.path.splitext(os.path.basename(source_file_name_with_path))[0]

    # Simplify the name
    simplified_name = f"{directory_name}_{file_name_without_ext}"

    # Format the counter as 000
    formatted_counter = f"{counter:03}"

    # Construct the file and prompt names
    file_name = f"{simplified_name}_{marker_name}_{unique_id}.part{formatted_counter}"
    prompt_file = f"{simplified_name}_{marker_name}_{unique_id}.prompt{formatted_counter}"

    return prompt_file, file_name

