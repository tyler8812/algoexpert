# O(n) time O(log(n)) space
def maxPathSum(tree):
    # Write your code here.
    _, max = maxSum(tree)
    return max


def maxSum(node):
    if node is None:
        return (0, -float("inf"))

    leftBranch, leftPath = maxSum(node.left)
    rightBranch, rightPath = maxSum(node.right)

    # 找左右最佳branch
    maxBranch = max(leftBranch, rightBranch)
    # 找currentNode最佳branch
    maxBranch = max(maxBranch + node.value, node.value)

    # current 最佳path
    maxPath = max(leftPath, rightPath, maxBranch,
                  leftBranch + node.value + rightBranch)
    return maxBranch, maxPath
