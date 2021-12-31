# O(nlog(n)) time O(n) space
def mergeOverlappingIntervals(intervals):
    # Write your code here.
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    answer = [sorted_intervals[0]]
    lastValue = sorted_intervals[0][1]

    for i in range(1, len(sorted_intervals)):
        if sorted_intervals[i][0] <= lastValue:
            # merge
            if sorted_intervals[i][1] > lastValue:
                temp = answer.pop()
                answer.append([temp[0], sorted_intervals[i][1]])
            else:
                continue

        else:
            answer.append(sorted_intervals[i])
        lastValue = sorted_intervals[i][1]

    return answer
