# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | O(1) space
def reverseLinkedList(head):

    prev_node, current_node = None, head
    while current_node.next is not None:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node
    current_node.next = prev_node

    return current_node
