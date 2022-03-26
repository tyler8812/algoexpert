# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | O(1) space
def removeKthNodeFromEnd(head, k):
    counter = 1
    first = head
    second = head
    while counter <= k:
        second = second.next
        counter += 1
    # remove the first index
    if second is None:
        head.value = head.next.value
        head.next = head.next.next
        return
    # remove other index
    while second.next is not None:
        first = first.next
        second = second.next
    first.next = first.next.next
