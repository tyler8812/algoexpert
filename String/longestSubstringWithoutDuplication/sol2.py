# O(n) time | O(min(n, a)) space


def longestSubstringWithoutDuplication(string):
    l, r = 0, 0
    visited = set()
    longest = ""
    while l <= r and r < len(string):
        while l < r and string[r] in visited:
            visited.remove(string[l])
            l += 1

        visited.add(string[r])
        longest = max(longest, string[l : r + 1], key=len)
        r += 1
    return longest


test = "clementisaczap"
longestSubstringWithoutDuplication(test)
