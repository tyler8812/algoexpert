# O(2^n * n) time | O(2^n * n) space
def powerset(array):
    subsets = [[]]
    for value in array:
        for i in range(len(subsets)):
            subsets.append(subsets[i] + [value])

    return subsets
