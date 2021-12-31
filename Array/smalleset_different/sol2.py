def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    # sort two array
    # sorting time complexity
    # O(nlog(n) + mlog(m)) time O(1) space
    arrayOne.sort()
    arrayTwo.sort()
    idx1 = 0
    idx2 = 0
    smallest = float("inf")
    answer = []
    while idx1 < len(arrayOne) and idx2 < len(arrayTwo):
        first = arrayOne[idx1]
        second = arrayTwo[idx2]

        if first < second:
            temp = second - first
            idx1 += 1
        elif first > second:
            temp = first - second
            idx2 += 1
        else:
            return [first, second]

        if temp < smallest:
            smallest = temp
            answer = [first, second]

    return answer
