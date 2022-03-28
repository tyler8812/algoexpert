# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n+m) time | O(1) space
def mergeLinkedLists(headOne, headTwo):
    current_one = headOne
    current_two = headTwo
    prev_one = None
    while current_one is not None and current_two is not None:
        if current_one.value < current_two.value:
            prev_one = current_one
            current_one = current_one.next
        else:
            if prev_one is not None:
                prev_one.next = current_two
            prev_one = current_two
            current_two = current_two.next
            prev_one.next = current_one
    if current_one is None:
        prev_one.next = current_two
    return headOne if headOne.value < headTwo.value else headTwo
