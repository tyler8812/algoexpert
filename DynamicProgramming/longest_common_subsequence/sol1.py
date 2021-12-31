# O(NM*min(N, M)) time O(NM*min(N, M)) space
def longestCommonSubsequence(str1, str2):
    lcs = [[[] for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i - 1] == str1[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + [str2[i - 1]]
                # ["A", "B", "C"] + ["D"] = ["A", "B", "C", "D"]
            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1], key=len)

    return lcs[-1][-1]
