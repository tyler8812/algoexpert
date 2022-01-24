# O(n! * n ) time | O(n! * n) space


def getPermutations(array):
    permutations = []
    permutationHelper(0, array, permutations)
    return permutations


def permutationHelper(index, array, permutations):
    if index == len(array) - 1:
        permutations.append(array.copy())
    else:
        for j in range(index, len(array)):
            swap(array, index, j)
            permutationHelper(index + 1, array, permutations)
            swap(array, index, j)


def swap(array, a, b):
    array[a], array[b] = array[b], array[a]


array = [1, 2, 3]
print(getPermutations(array))
