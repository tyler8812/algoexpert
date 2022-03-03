class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        queue = [self]

        while len(queue) > 0:
            array.append(queue[0].name)
            for child in queue[0].children:
                queue.append(child)
            queue.pop(0)
        return array
