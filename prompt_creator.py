
from settings import (MARKERS,
                        CREATE_FILE_NAME_AND_PROMPT_FILE,
                        PROMPT_TEMPLATES_PATH, 
                        PROMPTS_PATH)
import os

def create_prompt(counter, unique_id, marker_name, 
                  source_file_name_with_path, code_segment):
    """
    Creates a prompt file for a specific marker.

    Args:
        counter (int): Counter for the file (formatted as 000).
        unique_id (str): A unique identifier for the file.
        marker_name (str): Marker name to identify the prompt.
        source_file_name_with_path (str): Full path of the source file.
        code_segment (str): Code segment to be included in the prompt.

    Returns:
        str: Path to the created prompt file.
    """
    # Load the prompt template for the given marker

    prompt_file = None
    name = None
    for marker in MARKERS.values():
        if marker["start"] == marker_name:
            prompt_file = os.path.join(PROMPT_TEMPLATES_PATH, marker["prompt"])
            name = marker["name"]
            break

    if not prompt_file:
        raise Exception(f"No prompt found for this marker: {marker_name}")

    # Generate the prompt file name and the file name to be mentioned in the prompt
    prompt_file_name, file_name_to_mention_in_prompt = CREATE_FILE_NAME_AND_PROMPT_FILE(
        counter, unique_id, name, source_file_name_with_path
    )

    # Load the prompt template
    with open(prompt_file, "r") as file:
        prompt_template = file.read()
    prompt = prompt_template.replace("<<<file_name>>>", file_name_to_mention_in_prompt).replace("<<<code>>>", code_segment)

    # Define the full path for the prompt file
    prompt_file_with_path = os.path.join(PROMPTS_PATH, prompt_file_name)

    # Ensure the output directory exists
    # os.makedirs(os.path.dirname(prompt_file_with_path), exist_ok=True)

    # Save the generated prompt to the file
    with open(prompt_file_with_path, "w") as file:
        file.write(prompt)

    return prompt_file_with_path