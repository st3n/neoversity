import os
import time
from threaded_search import threaded_search
from multiprocess_search import multiprocess_search
from random_data import generate_files


def main():
    # Визначення вихідної директорії
    current_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(current_dir, "text_files")
    os.makedirs(output_dir, exist_ok=True)

    output_dir = "text_files"
    generate_files(output_dir)

    # Список файлів і ключових слів для пошуку
    file_paths = [os.path.join(output_dir, f) for f in os.listdir(output_dir)]
    keywords = ["Dream", "option", "also", "social"]

    # Багатопотокова обробка
    try:
        start_time = time.time()
        threaded_results = threaded_search(file_paths, keywords)
        end_time = time.time()
        print(f"Threaded search took {end_time - start_time:.2f} seconds")
        print(threaded_results)
    except Exception as e:
        print(f"An error occurred during threaded search: {e}")

    # Багатопроцесорна обробка
    try:
        start_time = time.time()
        multiprocess_results = multiprocess_search(file_paths, keywords)
        end_time = time.time()
        print(f"Multiprocess search took {end_time - start_time:.2f} seconds")
        print(multiprocess_results)
    except Exception as e:
        print(f"An error occurred during multiprocess search: {e}")


if __name__ == "__main__":
    main()

"""
Threaded search took 0.00 seconds
{'also': ['text_files/file_7.txt', 'text_files/file_20.txt', 'text_files/file_9.txt', 'text_files/file_16.txt'],
'social': ['text_files/file_6.txt', 'text_files/file_20.txt'], 'option': ['text_files/file_10.txt', 'text_files/file_16.txt']}
Multiprocess search took 0.11 seconds
{'also': ['text_files/file_7.txt', 'text_files/file_9.txt', 'text_files/file_20.txt', 'text_files/file_16.txt'],
'social': ['text_files/file_6.txt', 'text_files/file_20.txt'], 'option': ['text_files/file_10.txt', 'text_files/file_16.txt']}
"""
