# This is an input class. Do not edit.
from pickle import TRUE


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# n is the length of first linked list
# m is the length of second linked list
# O(max(n, m)) time | O(max(m, n)) space
def sumOfLinkedLists(linkedListOne, linkedListTwo):
    new_linked_list = LinkedList(0)
    current_node = new_linked_list
    carry = 0
    while True:
        adding = 0
        check_if_break = TRUE
        if linkedListOne is not None:
            adding += linkedListOne.value
            linkedListOne = linkedListOne.next
            check_if_break = False
        if linkedListTwo is not None:
            adding += linkedListTwo.value
            linkedListTwo = linkedListTwo.next
            check_if_break = False
        if carry != 0:
            adding += carry
            check_if_break = False
        if check_if_break:
            break
        if adding >= 10:
            adding = adding - 10
            carry = 1
        else:
            carry = 0
        new_node = LinkedList(adding)
        current_node.next = new_node
        current_node = current_node.next

    return new_linked_list.next
