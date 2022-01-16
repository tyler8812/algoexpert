# O(nlogn) time | O(n) space
def taskAssignment(k, tasks):
    answer = []
    taskDurationToIndices = getTaskDurationToIndices(tasks)
    sortedDuration = sorted(tasks)

    for i in range(k):
        task1Duration = sortedDuration[i]
        task1Index = taskDurationToIndices[task1Duration].pop()

        task2Duration = sortedDuration[-1 - i]
        task2Index = taskDurationToIndices[task2Duration].pop()

        answer.append([task1Index, task2Index])

    return answer


def getTaskDurationToIndices(tasks):
    taskDurationToIndices = {}

    for idx, taskDuration in enumerate(tasks):
        if taskDuration in taskDurationToIndices:
            taskDurationToIndices[taskDuration].append(idx)
        else:
            taskDurationToIndices[taskDuration] = [idx]

    return taskDurationToIndices
