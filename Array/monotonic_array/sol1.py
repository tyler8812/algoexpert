def isMonotonic(array):
    # Write your code here.
    # O(n) time O(1) space
    status = -1

    for i in range(1, len(array)):

        if array[i] - array[i-1] > 0:
            if status == -1:
                status = 1
            elif status == 0:
                return False
        elif array[i] - array[i-1] < 0:
            if status == -1:
                status = 0
            elif status == 1:
                return False

    return True
