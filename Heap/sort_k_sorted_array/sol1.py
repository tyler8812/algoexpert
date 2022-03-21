# O(nlog(k)) time | O(k) space (heap)
def sortKSortedArray(array, k):
    min_heap_with_k_elements = MinHeap(array[: min(k + 1, len(array))])
    next_idx_to_insert = 0
    # this for loop will insert all the array value to heap
    for idx in range(k + 1, len(array)):
        min_element = min_heap_with_k_elements.remove()
        array[next_idx_to_insert] = min_element
        next_idx_to_insert += 1
        min_heap_with_k_elements.insert(array[idx])

    # add remain value in heap to final sorted array
    while not min_heap_with_k_elements.is_empty():
        min_element = min_heap_with_k_elements.remove()
        array[next_idx_to_insert] = min_element
        next_idx_to_insert += 1

    return array


class MinHeap:
    def __init__(self, array):
        self.heap = self.build_heap(array)

    def is_empty(self):
        return len(self.heap) == 0

    def build_heap(self, array):
        first_parent_idx = (len(array) - 1 - 1) // 2
        for current_idx in reversed(range(first_parent_idx + 1)):
            self.sift_down(current_idx, len(array) - 1, array)
        return array

    def sift_down(self, current_idx, end_idx, heap):

        child_one_idx = current_idx * 2 + 1
        while child_one_idx <= end_idx:
            child_two_idx = (
                current_idx * 2 + 2 if current_idx * 2 + 2 <= end_idx else -1
            )

            if child_two_idx != -1 and heap[child_two_idx] < heap[child_one_idx]:
                idx_to_swap = child_two_idx
            else:
                idx_to_swap = child_one_idx

            if heap[current_idx] > heap[idx_to_swap]:
                self.swap(current_idx, idx_to_swap, heap)
                current_idx = idx_to_swap
                child_one_idx = current_idx * 2 + 1
            else:
                return

    def sift_up(self, current_idx, heap):
        parent_idx = (current_idx - 1) // 2
        while current_idx > 0 and heap[current_idx] < heap[parent_idx]:
            self.swap(current_idx, parent_idx, heap)
            current_idx = parent_idx
            parent_idx = (current_idx - 1) // 2

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        value_to_remove = self.heap.pop()
        self.sift_down(0, len(self.heap) - 1, self.heap)
        return value_to_remove

    def insert(self, value):
        self.heap.append(value)
        self.sift_up(len(self.heap) - 1, self.heap)

    def swap(self, i, j, array):
        array[i], array[j] = array[j], array[i]
