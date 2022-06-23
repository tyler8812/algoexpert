# O(n^2) time | O(n) sapce
def nextGreaterElement(array):
    answer = []
    for i in range(len(array)):
        flag = True
        for j in range(i + 1, i + len(array)):
            idx = j % len(array)
            if array[idx] > array[i]:
                flag = False
                answer.append(array[idx])
                break
        if flag:
            answer.append(-1)
    return answer


test = [2, 5, -3, -4, 6, 7, 2]
print(nextGreaterElement(test))
