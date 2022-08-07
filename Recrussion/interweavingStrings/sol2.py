# O(nm) time | O(nm)
# n: length of first string
# m: length of second string
def interweavingStrings(one, two, three):

    if len(three) != len(one) + len(two):
        return False
    cache = [[None for j in range(len(two) + 1)] for i in range(len(one) + 1)]
    print(cache)
    return are_inter_woven(one, two, three, 0, 0)


def are_inter_woven(one, two, three, i, j, cache):
    if cache[i][j] is not None:
        return cache[i][j]

    k = i + j
    if len(three) == k:
        return True

    if i < len(one) and one[i] == three[k]:
        cache[i][j] = are_inter_woven(one, two, three, i + 1, j, cache)
        if cache[i][j]:
            return True

    if j < len(two) and two[j] == three[k]:
        cache[i][j] = are_inter_woven(one, two, three, i, j + 1, cache)
        return cache[i][j]

    cache[i][j] = False
    return False


one = "algoexpert"
two = "your-dream-job"
three = "your-algodream-expertjob"
interweavingStrings(one, two, three)
