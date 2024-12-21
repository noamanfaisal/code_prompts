from settings import MARKERS
from copy import deepcopy

def extract_code_segments(file_path):
    """
    Extract code segments within a specific marker and yield them one by one.

    Args:
        file_path (str): The path to the file.
        marker_name (str): The name of the marker to extract.

    Yields:
        tuple: A tuple containing (marker_name, code_segment).
    """

    start_markers = [marker_data["start"] for marker_data in MARKERS.values()]

    end_markers = [marker_data["end"] for marker_data in MARKERS.values()]

    current_segment = []
    inside_marker = False
    start_marker = ''
    with open(file_path, "r") as file:
        for line in file:
            if line.strip() in start_markers:
                start_marker = deepcopy(line.strip())
                inside_marker = True
                current_segment = []
            elif line.strip() in end_markers and inside_marker:
                yield file_path, start_marker, "".join(current_segment)
                start_marker = ''
                inside_marker = False
            elif inside_marker:
                current_segment.append(line)
