# Do not edit the class below except for
# the insert method. Feel free to add new
# properties and methods to the class.
class ContinuousMedianHandler:
    def __init__(self):
        # Write your code here.
        self.median = None
        self.array = []

    # O(n) time
    def insert(self, number):
        index = len(self.array)
        for i in range(len(self.array)):
            if self.array[i] > number:
                index = i
                break
        if index == len(self.array):
            self.array = self.array + [number]
        else:
            self.array = self.array[:index] + [number] + self.array[index:]

    def getMedian(self):

        length = len(self.array)
        if length % 2 == 0:
            self.median = (self.array[length // 2 - 1] + self.array[length // 2]) / 2
        else:
            self.median = self.array[length // 2]
        return self.median
