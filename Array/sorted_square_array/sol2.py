def sortedSquaredArray(array):
    # Write your code here.
    # O(n) time O(n) space
    startIdx = 0
    lastIdx = len(array)-1
    answer = [0 for _ in array]
    for idx in reversed(range(len(array))):
        if abs(array[startIdx]) < abs(array[lastIdx]):
            answer[idx] = array[lastIdx] * array[lastIdx]
            lastIdx -= 1
        else:
            answer[idx] = array[startIdx] * array[startIdx]
            startIdx += 1

    return answer
