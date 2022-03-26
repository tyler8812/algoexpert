# This is an input class. Do not edit.
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

    node_one = linkedListOne
    node_two = linkedListTwo
    while node_one is not None or node_two is not None or carry != 0:
        value_one = node_one.value if node_one is not None else 0
        value_two = node_two.value if node_two is not None else 0
        adding = value_one + value_two + carry
        carry = adding // 10
        adding = adding % 10

        new_node = LinkedList(adding)
        current_node.next = new_node
        current_node = current_node.next
        node_one = node_one.next if node_one is not None else None
        node_two = node_two.next if node_two is not None else None

    return new_linked_list.next
