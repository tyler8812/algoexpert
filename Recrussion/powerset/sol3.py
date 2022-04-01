# O(2^n * n) time | O(2^n * n) space
def powerset(array):
    subsets = []
    new_subsets = helper(0, array, [], subsets)
    return new_subsets


def helper(idx, array, current_subset, subsets):

    if idx == len(array):
        new_subsets = subsets.copy()
        new_subsets.append(current_subset.copy())

    else:
        new_subsets = helper(idx + 1, array, current_subset.copy(), subsets)
        current_subset.append(array[idx])
        new_subsets = helper(idx + 1, array, current_subset.copy(), new_subsets)
    return new_subsets
