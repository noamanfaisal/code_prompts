import os
import argparse

def merge_files(input_path, output_path, uuid, output_name):
    """
    Merge files with the specified UUID from the input path and save the merged file 
    in the output path.

    Args:
        input_path (str): The root directory to search for files.
        output_path (str): The directory where the merged file will be saved.
        uuid (str): The UUID to identify the parts of the file to merge.
        output_name (str): The name of the merged output file.

    Returns:
        None
    """
    # Check if input path exists
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input path '{input_path}' does not exist.")

    # Check if output path exists
    if not os.path.exists(output_path):
        raise FileNotFoundError(f"Output path '{output_path}' does not exist.")

    # Collect all files with the given UUID
    files_to_merge = []
    for root, _, files in os.walk(input_path):
        for file in files:
            if uuid in file:
                files_to_merge.append(os.path.join(root, file))

    if not files_to_merge:
        raise ValueError(f"No files found with UUID '{uuid}'\
                          in the input path '{input_path}'.")

    # Extract part numbers from file names
    actual_parts = sorted([int(f.split('part')[-1]) for f in files_to_merge])

    # Generate the expected parts directly from the actual parts
    expected_parts = list(range(min(actual_parts), max(actual_parts) + 1))

    # Check if the lists match
    missing_parts = set(expected_parts) - set(actual_parts)
    if missing_parts:
        raise ValueError(f"Missing parts: {sorted(missing_parts)}.")

    files_to_merge = []
    for root, _, files in os.walk(input_path):
        for file in files:
            if uuid in file:
                files_to_merge.append(os.path.join(root, file))

    # Sort files by part number (e.g., part000, part001)

    files_to_merge.sort(key=lambda x: int(x.split('part')[-1]))

    # Output file path
    output_file_path = os.path.join(output_path, output_name)

    with open(output_file_path, 'w') as output_file:
        for index, file_path in enumerate(files_to_merge, start=1):
            # Add a comment for the part being merged
            output_file.write(f"#### Part {index} - UUID {uuid} ####\n")

            # Read and write the content of each part
            with open(file_path, 'r') as part_file:
                output_file.write(part_file.read())
                output_file.write("\n")  # Ensure a newline between parts

    print(f"Merged {len(files_to_merge)} files into {output_file_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge files with a specific UUID.")
    parser.add_argument("input_path", type=str, help="Path to the input directory containing files.")
    parser.add_argument("output_path", type=str, help="Path to the output directory.")
    parser.add_argument("uuid", type=str, help="UUID to search for in file names.")
    parser.add_argument("output_name", type=str, help="Name of the merged output file.")

    args = parser.parse_args()

    merge_files(
        input_path=args.input_path,
        output_path=args.output_path,
        uuid=args.uuid,
        output_name=args.output_name
    )
