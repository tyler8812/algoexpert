# O(n^3) time | O(n) space
def longestPalindromicSubstring(string):
    longest = ""
    for i in range(len(string)):
        for j in range(i, len(string)):

            substring = string[i : j + 1]
            if len(substring) > len(longest) and is_palindromic(substring):
                longest = substring
    return longest


def is_palindromic(string):
    left_idx = 0
    right_idx = len(string) - 1
    while left_idx < right_idx:
        if string[left_idx] != string[right_idx]:
            return False
        left_idx += 1
        right_idx -= 1

    return True
