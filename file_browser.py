
import os

def browse_files(folder_path, match_condition=None):
    """
    Recursively browse a folder and return files that match a specific condition.

    Args:
        folder_path (str): The root folder to start browsing.
        match_condition (function): A function that takes a file path as input and returns 
        True if it matches the condition.

    Returns:
        list: A list of file paths that match the condition.
    """
    matched_files = []
    
    # Default match condition: all files
    if match_condition is None:
        match_condition = lambda file_path: True

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if match_condition(file_path):
                matched_files.append(file_path)
    
    return matched_files

# Example Usage

# Define a match condition: filter files with ".py" extension
def is_python_file(file_path):
    return file_path.endswith('.py')

# Call the function
folder_path = "/path/to/your/folder"  # Replace with your folder path
python_files = browse_files(folder_path, match_condition=is_python_file)

print(f"Found {len(python_files)} Python files:")
for file in python_files:
    print(file)
