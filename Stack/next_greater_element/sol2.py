# O(n) time | O(n) sapce
# Stack
def nextGreaterElement(array):
    answer = [-1] * len(array)
    stack = []
    for i in range(2 * len(array)):
        idx = i % len(array)

        while len(stack) > 0 and array[idx] > array[stack[-1]]:
            top = stack.pop()
            answer[top] = array[idx]
        stack.append(idx)
        print(answer)

    return answer


test = [2, 5, -3, -4, 6, 7, 2]
print(nextGreaterElement(test))
