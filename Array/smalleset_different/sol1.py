def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    # O(n^2) time O(1) space
    smallest = float("inf")
    array1Idx = -1
    array2Idx = -1
    for i in range(0, len(arrayOne)):
        for j in range(0, len(arrayTwo)):
            temp = abs(arrayOne[i] - arrayTwo[j])
            if temp < smallest:
                array1Idx = i
                array2Idx = j
                smallest = temp

    return [arrayOne[array1Idx], arrayTwo[array2Idx]]
