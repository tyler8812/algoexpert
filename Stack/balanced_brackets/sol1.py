# O(n) time | O(n) space
def balancedBrackets(string):
    stack = []
    matching = {")": "(", "]": "[", "}": "{"}
    open_bracker = ["(", "[", "{"]
    close_bracker = [")", "]", "}"]
    for char in string:
        if char in open_bracker:
            stack.append(char)
        elif char in close_bracker:
            if len(stack) == 0:
                return False
            if stack[-1] == matching[char]:
                stack.pop()
            else:
                return False

    return len(stack) == 0


test = "([])(){}(())()()"

balancedBrackets(test)
