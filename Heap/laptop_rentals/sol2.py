# O(nlog(n)) time | O(n) space
def laptopRentals(times):
    times.sort(key=lambda x: x[0])
    min_heap = MinHeap([])
    for time in times:
        if min_heap.length == 0:
            min_heap.insert(time)
        else:
            min_time_in_heap = min_heap.peek()

            # compare end time and start time of new interval
            if min_time_in_heap[1] <= time[0]:
                min_heap.remove()

            min_heap.insert(time)

    return min_heap.length


class MinHeap:
    def __init__(self, array) -> None:
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
            if child_twoIdx != -1 and heap[child_twoIdx][1] < heap[child_oneIdx][1]:
                idx_to_swap = child_twoIdx
            else:
                idx_to_swap = child_oneIdx
            if heap[idx_to_swap][1] < heap[currentIdx][1]:
                self.swap(idx_to_swap, currentIdx, heap)
                currentIdx = idx_to_swap
                child_oneIdx = currentIdx * 2 + 1
            else:
                return

    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0:
            if heap[currentIdx][1] < heap[parentIdx][1]:
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


times = [
    [1, 3],
    [2, 5],
    [4, 5],
    [0, 20],
    [1, 10],
    [10, 20],
    [11, 15],
    [12, 13],
    [0, 1],
    [0, 2],
]

print(laptopRentals(times))
