# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
    pointer1 = head.next
    pointer2 = head.next.next
    # 第一次碰到
    while pointer1 != pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next.next

    # 把pointer拉到head再做一次iterate，去碰地2次。
    pointer1 = head
    while pointer1 != pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1
