def longestPeak(array):
    # O(n) time O(1) space
    # finite state machine
    longestPeak = 0
    status = 0
    tempPeak = 0
    for i in range(0, len(array)-1):
        if status == 0:
            if array[i+1] > array[i]:
                status = 1
                tempPeak = 1
            elif array[i+1] < array[i]:
                status = 2
        elif status == 1:
            if array[i+1] == array[i]:
                status = 0
                tempPeak = 0
            elif array[i+1] < array[i]:
                status = 3
                tempPeak += 1
            else:
                tempPeak += 1

        elif status == 2:
            if array[i+1] == array[i]:
                status = 0
            elif array[i+1] > array[i]:
                status = 1
                tempPeak += 1
        elif status == 3:
            if array[i+1] > array[i]:
                if tempPeak + 1 > longestPeak:
                    longestPeak = tempPeak + 1
                tempPeak = 1
                status = 1
            elif array[i+1] < array[i]:
                tempPeak += 1
            else:
                status = 0
                if tempPeak + 1 > longestPeak:
                    longestPeak = tempPeak + 1
                tempPeak = 0
        else:
            print("error")

    if status == 1 or status == 3:
        if array[-1] < array[-2]:
            return tempPeak + 1 if tempPeak + 1 > longestPeak else longestPeak

    return longestPeak
