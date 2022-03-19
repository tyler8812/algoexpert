# O(log(n)) time | O(n) space
def MAX_HEAP_FUNC(a, b):
    return a > b


def MIN_HEAP_FUNC(a, b):
    return a < b


class ContinuousMedianHandler:
    def __init__(self):
        # 建立一個min heap和max heap分別代表中位數左有兩邊。
        self.lowers = Heap(MAX_HEAP_FUNC, [])
        self.greaters = Heap(MIN_HEAP_FUNC, [])
        self.median = None

    def insert(self, number):
        # 判斷lowers是不是空的或是叫加入的數字小於lower的root。
        if not self.lowers.length or number < self.lowers.peek():
            self.lowers.insert(number)
        else:
            self.greaters.insert(number)
        self.reblance_heaps()
        self.update_median()

    def reblance_heaps(self):
        if self.lowers.length - self.greaters.length == 2:
            self.greaters.insert(self.lowers.remove())
        elif self.greaters.length - self.lowers.length == 2:
            self.lowers.insert(self.greaters.remove())

    def update_median(self):
        if self.lowers.length == self.greaters.length:
            self.median = (self.lowers.peek() + self.greaters.peek()) / 2
        elif self.lowers.length < self.greaters.length:
            self.median = self.greaters.peek()
        else:
            self.median = self.lowers.peek()

    def getMedian(self):
        return self.median


class Heap:
    def __init__(self, comparision_func, array) -> None:
        self.comparison_func = comparision_func
        self.heap = self.buildHeap(array)
        self.length = len(self.heap)

    def buildHeap(self, array):
        first_parentIdx = (len(array) - 1 - 1) // 2
        for currentIdx in reversed(range(first_parentIdx + 1)):
            self.siftDown(currentIdx, len(array) - 1, array)
        return array

    def siftDown(self, currentIdx, endIdx, heap):
        child_oneIdx = currentIdx * 2 + 1
        while child_oneIdx <= endIdx:
            child_twoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
            if child_twoIdx != -1:
                if self.comparison_func(heap[child_oneIdx], heap[child_twoIdx]):
                    idx_to_swap = child_oneIdx
                else:
                    idx_to_swap = child_twoIdx
            else:
                idx_to_swap = child_oneIdx
            if self.comparison_func(heap[idx_to_swap], heap[currentIdx]):
                self.swap(currentIdx, idx_to_swap, heap)
                currentIdx = idx_to_swap
                child_oneIdx = currentIdx * 2 + 1
            else:
                return

    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0:
            if self.comparison_func(heap[currentIdx], heap[parentIdx]):
                self.swap(currentIdx, parentIdx, heap)
                currentIdx = parentIdx
                parentIdx = (currentIdx - 1) // 2
            else:
                return

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, self.length - 1, self.heap)
        value_to_remove = self.heap.pop()
        self.length -= 1
        self.siftDown(0, self.length - 1, self.heap)
        return value_to_remove

    def insert(self, value):
        self.heap.append(value)
        self.length += 1
        self.siftUp(self.length - 1, self.heap)

    def swap(self, i, j, array):
        array[i], array[j] = array[j], array[i]
