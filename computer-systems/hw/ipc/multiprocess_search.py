import multiprocessing
from multiprocessing import Queue


def search_keywords(file_path, keywords, queue):
    try:
        result = {}
        with open(file_path, "r") as f:
            content = f.read()
            for keyword in keywords:
                if keyword in content:
                    if keyword not in result:
                        result[keyword] = []
                    result[keyword].append(file_path)
        queue.put(result)
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")


def worker(files, keywords, queue):
    for file_path in files:
        search_keywords(file_path, keywords, queue)


def multiprocess_search(file_paths, keywords):
    processes = []
    queue = Queue()
    results = {}

    num_processes = 4
    files_per_process = len(file_paths) // num_processes
    for i in range(num_processes):
        start = i * files_per_process
        end = None if i == num_processes - 1 else (i + 1) * files_per_process
        process = multiprocessing.Process(
            target=worker, args=(file_paths[start:end], keywords, queue)
        )
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    while not queue.empty():
        result = queue.get()
        for keyword, files in result.items():
            if keyword not in results:
                results[keyword] = []
            results[keyword].extend(files)

    return results
