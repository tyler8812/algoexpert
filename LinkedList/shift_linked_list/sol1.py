# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | O(1) space
def shiftLinkedList(head, k):
    list_length = 1
    list_tail = head
    while list_tail.next is not None:
        list_tail = list_tail.next
        list_length += 1

    offset = abs(k) % list_length
    if offset == 0:
        return head
    new_tail_position = list_length - offset if k > 0 else offset
    new_tail = head
    for _ in range(1, new_tail_position):
        new_tail = new_tail.next
    new_head = new_tail.next
    new_tail.next = None
    list_tail.next = head
    return new_head
