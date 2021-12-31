# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# O(n) time O(d) space  n all node, d depth of BST(call stack)
def validateBst(node):
    return validateNode(node, float("-inf"), float("inf"))


def validateNode(node, minV, maxV):
    if node is None:
        return True

    if node.value < minV or node.value >= maxV:
        return False
    leftvalid = validateNode(node.left, minV, node.value)
    return leftvalid and validateNode(node.right, node.value, maxV)
