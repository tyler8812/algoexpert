# O(n^2) time | O(n) space
def sortStack(stack):
    if len(stack) == 0:
        return stack

    top = stack.pop()

    sortStack(stack)

    insert_to_stack(stack, top)

    return stack


def insert_to_stack(stack, value):
    if len(stack) == 0 or stack[-1] < value:
        stack.append(value)
        return
    top = stack.pop()
    insert_to_stack(stack, value)
    stack.append(top)


test = [-5, 2, -2, 4, 3, 1]


output = sortStack(test)
print(output)
