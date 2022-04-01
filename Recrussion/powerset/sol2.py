# O(2^n * n) time | O(2^n * n) space
def powerset(array, idx=None):
    if idx is None:
        idx = len(array) - 1
    if idx < 0:
        return [[]]

    element = array[idx]
    subsets = powerset(array, idx - 1)
    for i in range(len(subsets)):
        subsets.append(subsets[i] + [element])
    return subsets
