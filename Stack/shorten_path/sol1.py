# O(n) time | O(n) space
def shortenPath(path):
    is_root = path[0] == "/"
    tokens = filter(is_important_token, path.split("/"))
    stack = []

    if is_root:
        stack.append("")

    for token in tokens:
        if token == "..":
            if len(stack) == 0 or stack[-1] == "..":
                stack.append(token)
            elif stack[-1] != "":
                stack.pop()
        else:
            stack.append(token)

    if len(stack) == 1 and stack[0] == "":
        return "/"

    return "/".join(stack)


def is_important_token(token):
    return len(token) > 0 and token != "."


# test = "/foo/../test/../test/../foo//bar/./baz"
# print(shortenPath(test))
