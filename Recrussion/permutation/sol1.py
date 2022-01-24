# O(n! * n^2 ) time | O(n! * n) space
# time: 總共有n!組合，所以會call permutation n!次 每次是 n^2
# space: 總共n!組合，每個包含n個value
def getPermutations(array):
    permutations = []
    permutationHelper(array, [], permutations)
    return permutations


def permutationHelper(array, currentPermutation, permutations):
    if len(array) == 0 and len(currentPermutation) > 0:
        permutations.append(currentPermutation)
    else:
        for i in range(len(array)):
            # O(n)
            newArray = array[:i] + array[i + 1 :]
            # O(n)
            newPermutation = currentPermutation + [array[i]]
            permutationHelper(newArray, newPermutation, permutations)


array = [1, 2, 3]
print(getPermutations(array))
