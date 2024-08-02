from heapq import heappush, heappop


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def merge_k_lists_recursion(lists):
    if not lists:
        return []

    def merge_range(lists, start, end):
        if start == end:
            return lists[start]
        if start < end:
            mid = (start + end) // 2
            left_merged = merge_range(lists, start, mid)
            right_merged = merge_range(lists, mid + 1, end)
            return merge(left_merged, right_merged)

    return merge_range(lists, 0, len(lists) - 1)


"""beautiful solution based on heap, gives N*log(k) time complexity"""


def merge_k_lists(lists):
    min_heap = []

    for i, lst in enumerate(lists):
        if lst:
            heappush(min_heap, (lst[0], i, 0))

    merged_list = []

    while min_heap:
        val, list_index, element_index = heappop(min_heap)
        merged_list.append(val)

        if element_index + 1 < len(lists[list_index]):
            next_val = lists[list_index][element_index + 1]
            heappush(min_heap, (next_val, list_index, element_index + 1))

    return merged_list


# example
lists = [
    [1, 7],
    [2, 3, 4],
    [2, 6, 9, 13, 19],
]
merged_list = merge_k_lists_recursion(lists)
print("sorted list: ", merged_list)
