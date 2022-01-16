# O(nlogn) time | O(1) space


def minimumWaitingTime(queries):
    sort_queries = sorted(queries)
    answer = 0
    length = len(queries)
    for i in range(length):
        answer += sort_queries[i] * (length - i - 1)
    return answer


print(minimumWaitingTime([3, 2, 1, 2, 6]))
