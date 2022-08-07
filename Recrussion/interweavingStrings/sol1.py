# O(2^(n+m)) time | O(n+m)
# n: length of first string
# m: length of second string
def interweavingStrings(one, two, three):
    if len(three) != len(one) + len(two):
        return False
    return are_inter_woven(one, two, three, 0, 0)


def are_inter_woven(one, two, three, i, j):
    k = i + j
    if len(three) == k:
        return True

    if i < len(one) and one[i] == three[k]:
        if are_inter_woven(one, two, three, i + 1, j):
            return True

    if j < len(two) and two[j] == three[k]:
        return are_inter_woven(one, two, three, i, j + 1)

    return False
