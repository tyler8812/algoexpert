# This is an input class. Do not edit.
# O(nk) time O(n) space
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findNodesDistanceK(tree, target, k):
    # Write your code here.
    dict = {}
    traversal(tree, dict, None)
    print(dict)
    answer = findKDistance(dict, k, target)
    return answer


def traversal(node, dict, parent):
    dict[node.value] = []
    if parent is not None:
        dict[node.value].append(parent.value)
    if(node.left):
        traversal(node.left, dict, node)
        dict[node.value].append(node.left.value)
    if(node.right):
        traversal(node.right, dict, node)
        dict[node.value].append(node.right.value)


def findKDistance(dict, k, target):
    queue = dict[target].copy()
    visited = set([target])
    for i in range(k-1):
        newQueue = []
        for node in queue:
            for newNode in dict[node]:
                if newNode not in visited:
                    newQueue.append(newNode)
            visited.add(node)
        queue = newQueue.copy()

    return queue
