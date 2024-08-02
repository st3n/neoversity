from sorting_algorithms import insertion_sort, merge_sort

import timeit
import random


def generate_data(size):
    return [random.randint(0, 10000) for _ in range(size)]


def measure_time(sort_function, data, number=1):
    return timeit.timeit(lambda: sort_function(data), number=number)


def main():
    data_sizes = [100, 1000, 10000, 100000]
    results = {}

    for size in data_sizes:
        data = generate_data(size)

        results[size] = {
            "insertion_sort": measure_time(insertion_sort, data),
            "merge_sort": measure_time(merge_sort, data),
            "timsort": measure_time(sorted, data),
        }

    for size, times in results.items():
        print(f"Array size: {size}")
        for algo, time_taken in times.items():
            print(f"  {algo}: {time_taken:.6f} seconds")


if __name__ == "__main__":
    main()

'''
Results:

Array size: 100
  insertion_sort: 0.000065 seconds
  merge_sort: 0.000048 seconds
  timsort: 0.000001 seconds
Array size: 1000
  insertion_sort: 0.009031 seconds
  merge_sort: 0.000579 seconds
  timsort: 0.000005 seconds
Array size: 10000
  insertion_sort: 0.904322 seconds
  merge_sort: 0.007428 seconds
  timsort: 0.000044 seconds
Array size: 100000
  insertion_sort: 91.991499 seconds
  merge_sort: 0.094548 seconds
  timsort: 0.000476 seconds

From these results, you can see that Timsort consistently performs better than both Insertion Sort and Merge Sort,
especially as the array size increases. This demonstrates why Timsort is used in Python's built-in sorting functions.
'''
