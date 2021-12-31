def quickselect(array, k):
    # Write your code here.
    # O(nk) time O(1) space
    for i in range(0, k):
        smallest = float("inf")
        smallestIdx = -1
        for j in range(0, len(array)):
            if array[j] < smallest:
                smallest = array[j]
                smallestIdx = j
        if i == k-1:
            return array[smallestIdx]
        else:
            del array[smallestIdx]
