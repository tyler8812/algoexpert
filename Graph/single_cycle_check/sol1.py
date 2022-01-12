# O(n) time | O(1) space
def hasSingleCycle(array):
    visitedTime = 0
    currentIdx = 0
    while visitedTime < len(array):
        if visitedTime > 0 and currentIdx == 0:
            return False
        visitedTime += 1
        currentIdx = goNextIdx(currentIdx, array)
        print(visitedTime, currentIdx)
    return True if currentIdx == 0 else False


def goNextIdx(currentIdx, array):
    nextIdx = (currentIdx + array[currentIdx]) % len(array)
    return nextIdx
