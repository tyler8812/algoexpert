# O(n) time O(1) space
def kadanesAlgorithm(array):
    maxAccumulateValue = array[0]
    accumulateValue = array[0]
    for i in range(1, len(array)):
        accumulateValue = max(accumulateValue + array[i], array[i])
        if maxAccumulateValue < accumulateValue:
            maxAccumulateValue = accumulateValue
    return maxAccumulateValue


array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
print(kadanesAlgorithm(array))
