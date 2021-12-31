# O(nm) time O(nm) space
def levenshteinDistance(str1, str2):
    str1 = " " + str1
    str2 = " " + str2
    array = [[0 for _ in range(len(str2))] for _ in range(len(str1))]
    for i in range(len(str1)):
        for j in range(len(str2)):
            if i == 0 and j == 0:
                array[i][j] = 0
            elif i == 0:
                array[i][j] = j
            elif j == 0:
                array[i][j] = i
            else:
                if str1[i] == str2[j]:
                    array[i][j] = array[i-1][j-1]
                else:
                    array[i][j] = min(
                        array[i-1][j-1], array[i-1][j], array[i][j-1]) + 1

    return array[-1][-1]


# str1 = "abc"
# str2 = "yabd"

# levenshteinDistance(str1, str2)
