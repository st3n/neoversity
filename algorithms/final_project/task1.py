class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sort(self):
        self.head = self._merge_sort(self.head)

    def _merge_sort(self, head):
        if not head or not head.next:
            return head

        middle = self._get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        left = self._merge_sort(head)
        right = self._merge_sort(next_to_middle)

        sorted_list = self._sorted_merge(left, right)
        return sorted_list

    def _get_middle(self, head):
        if head is None:
            return head

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def _sorted_merge(self, left, right):
        if not left:
            return right
        if not right:
            return left

        if left.value <= right.value:
            result = left
            result.next = self._sorted_merge(left.next, right)
        else:
            result = right
            result.next = self._sorted_merge(left, right.next)

        return result

    def merge_sorted(self, other):
        self.head = self._sorted_merge(self.head, other.head)

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result


# Приклад використання:
list1 = LinkedList()
list1.append(3)
list1.append(1)
list1.append(4)
list1.append(2)

print("Original list:")
print(list1.to_list())

list1.reverse()
print("Reversed list:")
print(list1.to_list())

list1.sort()
print("Sorted list:")
print(list1.to_list())

list2 = LinkedList()
list2.append(5)
list2.append(6)

list1.merge_sorted(list2)
print("Merged sorted list:")
print(list1.to_list())

"""
Original list:
[3, 1, 4, 2]
Reversed list:
[2, 4, 1, 3]
Sorted list:
[1, 2, 3, 4]
Merged sorted list:
[1, 2, 3, 4, 5, 6]
"""
