# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self):
        self.min = []
        self.max = []
        self.stack = []

    def peek(self):

        return self.stack[len(self.stack) - 1]

    def pop(self):
        self.min.pop()
        self.max.pop()
        return self.stack.pop()

    def push(self, number):

        if len(self.min):
            self.min.append(min(self.min[len(self.min) - 1], number))
            self.max.append(max(self.max[len(self.max) - 1], number))
        else:
            self.min.append(number)
            self.max.append(number)
        self.stack.append(number)

    def getMin(self):

        return self.min[len(self.min) - 1]

    def getMax(self):

        return self.max[len(self.max) - 1]
