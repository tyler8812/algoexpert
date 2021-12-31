# O(nm) time O(min(n,m)) space
def levenshteinDistance(str1, str2):
    str1 = " " + str1
    str2 = " " + str2
    if len(str1) >= len(str2):
        long = str1
        short = str2
    else:
        long = str2
        short = str1
    first = [x for x in range(len(short))]
    for i in range(1, len(long)):
        second = [None for _ in range(len(short))]
        second[0] = i
        for j in range(1, len(short)):
            if long[i] == short[j]:
                second[j] = first[j-1]
            else:
                second[j] = min(
                    first[j-1], first[j], second[j-1]) + 1
        first = second.copy()
    return second[-1] if len(long) > 1 else first[-1]


str1 = "abc"
str2 = "yabd"

levenshteinDistance(str1, str2)
