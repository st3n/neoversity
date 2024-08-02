import os
import shutil
import argparse


def recursive_copy(source_dir, destination_dir):
    if not os.path.isdir(source_dir):
        raise ValueError

    for root, dirs, files in os.walk(source_dir):
        for file in files:
            source_file_path = os.path.join(root, file)
            dest_dir = os.path.join(destination_dir, os.path.splitext(file)[1][1:])
            os.makedirs(dest_dir, exist_ok=True)
            dest_file_path = os.path.join(dest_dir, file)
            shutil.copy2(source_file_path, dest_file_path)
            print(f"Copied '{source_file_path}' to '{dest_file_path}'")
        for dir in dirs:
            source_sub_dir = os.path.join(root, dir)
            # Recursively call the function for subdirectories
            recursive_copy(source_sub_dir, destination_dir)


def main(source_dir, destination_dir):
    try:
        # very naive
        source_dir = os.path.abspath(source_dir)
        destination_dir = os.path.abspath(destination_dir)
        recursive_copy(source_dir, destination_dir)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Copy and sort files recursively.")
    parser.add_argument("source_dir", help="Path to the source directory.")
    parser.add_argument(
        "destination_dir",
        nargs="?",
        default="dist",
        help="Path to the destination directory. Default is 'dist'.",
    )
    args = parser.parse_args()

    source_dir = args.source_dir
    destination_dir = args.destination_dir

    main(source_dir, destination_dir)
