def quickselect(array, k):
    # Write your code here.
    # O(nlogn) time O(1)space

    # you can just sort and output the answer
    array.sort()
    return array[k-1]
