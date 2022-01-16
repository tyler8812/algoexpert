# O(nlogn) time | O(n) space
def taskAssignment(k, tasks):
    sorted_index = sorted(range(len(tasks)), key=lambda k: tasks[k])
    answer = []
    for i in range(k):
        answer.append([sorted_index[i], sorted_index[-1 - i]])
    return answer


print(taskAssignment(3, [1, 3, 5, 3, 1, 4]))
