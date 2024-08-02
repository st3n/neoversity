import threading


def search_keywords(file_path, keywords, results):
    try:
        with open(file_path, "r") as f:
            content = f.read()
            for keyword in keywords:
                if keyword in content:
                    if keyword not in results:
                        results[keyword] = []
                    results[keyword].append(file_path)
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")


def threaded_search(file_paths, keywords):
    threads = []
    results = {}

    def worker(files):
        for file_path in files:
            search_keywords(file_path, keywords, results)

    num_threads = 4
    files_per_thread = len(file_paths) // num_threads
    for i in range(num_threads):
        start = i * files_per_thread
        end = None if i == num_threads - 1 else (i + 1) * files_per_thread
        thread = threading.Thread(target=worker, args=(file_paths[start:end],))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return results
