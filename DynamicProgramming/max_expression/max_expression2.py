
def maximizeExpression(array):
    # Write your code here.
    # 	O(n)time O(n)space
    # dynamic
    import math
    if len(array) < 4:
        return 0

    maxOfA = [array[0]]
    maxOfAMinusB = [-math.inf]
    maxOfAMinusBPlusC = [-math.inf] * 2
    maxOfAMinusBPlusCMinusD = [-math.inf] * 3
    print(maxOfAMinusBPlusC)
    print(maxOfAMinusBPlusCMinusD)

    for idx in range(1, len(array)):
        currentMax = max(maxOfA[idx-1], array[idx])
        maxOfA.append(currentMax)

    for idx in range(1, len(array)):
        currentMax = max(maxOfAMinusB[idx-1], maxOfA[idx-1] - array[idx])
        maxOfAMinusB.append(currentMax)

    for idx in range(2, len(array)):
        currentMax = max(
            maxOfAMinusBPlusC[idx-1], maxOfAMinusB[idx-1] + array[idx])
        maxOfAMinusBPlusC.append(currentMax)

    for idx in range(3, len(array)):
        currentMax = max(
            maxOfAMinusBPlusCMinusD[idx-1], maxOfAMinusBPlusC[idx-1] - array[idx])
        maxOfAMinusBPlusCMinusD.append(currentMax)
    # print(maxOfAMinusBPlusCMinusD)
    return maxOfAMinusBPlusCMinusD[-1]


print(maximizeExpression([3, 6, 1, -3, 2, 7]))
