def isMonotonic(array):
    # Write your code here.
    # O(n) time O(1) space
    if len(array) <= 2:
        return True

    direction = array[1] - array[0]
    for i in range(2, len(array)):
        if direction == 0:
            direction = array[i] - array[i-1]
            continue
        if directionDifferent(direction, array[i], array[i-1]):
            return False

    return True


def directionDifferent(direction, a, b):
    if direction < 0:
        return a - b > 0
    return a - b < 0
