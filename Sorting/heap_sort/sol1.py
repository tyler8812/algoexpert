# O(1) space | O(nlog(n)) time
def heapSort(array):
    build_max_heap(array)
    # start from final idx of array and swap it with the root(biggest value)
    for end_idx in reversed(range(1, len(array))):
        swap(0, end_idx, array)
        sift_down(0, end_idx - 1, array)

    return array


def build_max_heap(array):
    first_parent_idx = (len(array)) // 2 - 1
    for current_idx in reversed(range(first_parent_idx + 1)):
        sift_down(current_idx, len(array) - 1, array)


def sift_down(current_idx, end_idx, heap):
    child_left = current_idx * 2 + 1
    while child_left <= end_idx:
        child_right = current_idx * 2 + 2 if current_idx * 2 + 2 <= end_idx else -1
        if child_right > -1 and heap[child_right] > heap[child_left]:
            idx_to_swap = child_right
        else:
            idx_to_swap = child_left
        if heap[current_idx] < heap[idx_to_swap]:
            swap(current_idx, idx_to_swap, heap)
            current_idx = idx_to_swap
            child_left = current_idx * 2 + 1
        else:
            return


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
