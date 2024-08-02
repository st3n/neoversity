import asyncio
import aiofiles
import os
import shutil
import argparse
import logging
from pathlib import Path


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Asynchronously sort files by extension."
    )
    parser.add_argument("source_folder", type=str, help="Path to the source folder.")
    parser.add_argument("output_folder", type=str, help="Path to the output folder.")
    return parser.parse_args()


def init_paths(source_folder, output_folder):
    source_path = Path(source_folder)
    output_path = Path(output_folder)
    if not source_path.is_dir():
        raise ValueError(
            f"Source folder {source_folder} does not exist or is not a directory."
        )
    output_path.mkdir(parents=True, exist_ok=True)
    return source_path, output_path


async def async_copy_folder_by_ext(source_path, output_path):
    tasks = []
    for item in source_path.iterdir():
        if item.is_dir():
            tasks.append(async_copy_folder_by_ext(item, output_path))
        else:
            tasks.append(copy_file(item, output_path))
    await asyncio.gather(*tasks)


async def copy_file(file_path, output_path):
    extension = file_path.suffix[1:]  # Get file extension without the dot
    target_dir = output_path / extension
    target_dir.mkdir(parents=True, exist_ok=True)
    target_path = target_dir / file_path.name
    async with aiofiles.open(file_path, "rb") as src_file:
        async with aiofiles.open(target_path, "wb") as dst_file:
            await dst_file.write(await src_file.read())


def setup_logging():
    logging.basicConfig(
        level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s"
    )


async def main():
    args = parse_arguments()
    source_path, output_path = init_paths(args.source_folder, args.output_folder)
    setup_logging()
    try:
        await async_copy_folder_by_ext(source_path, output_path)
    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    asyncio.run(main())


"""
❯ python task1.py source_folder dest_folder/                                                                                                                                                   /0.1s
❯ ls
dest_folder  source_folder  task1.py                                                                                                                                                           /0.0s
❯ tree dest_folder/
dest_folder/
├── bin
│   └── dummy.bin
├── py
│   └── empty.py
├── txt
│   └── some_test.txt
└── yaml
    └── foo.yaml

5 directories, 4 files
"""
