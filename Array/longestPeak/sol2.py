def longestPeak(array):
    # split to two task
    # 1) find peak: compare the right and the left of the index,
    # if it is a peak, the index should larger than right and left index.
    # 2) compare peak
    # O(n) time O(1) space
    longestPeakLength = 0
    i = 1
    while i < len(array) - 1:
        isPeak = array[i-1] < array[i] and array[i+1] < array[i]
        if not isPeak:
            i += 1
            continue

        leftIdx = i - 2
        while leftIdx >= 0 and array[leftIdx] < array[leftIdx+1]:
            leftIdx -= 1
        rightIdx = i + 2
        while rightIdx < len(array) and array[rightIdx] < array[rightIdx-1]:
            rightIdx += 1

        currentPeakLength = rightIdx - leftIdx - 1
        longestPeakLength = max(longestPeakLength, currentPeakLength)

        i = rightIdx

    return longestPeakLength
