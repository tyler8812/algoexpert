# O(n^2) time | O(n) space
def longestPalindromicSubstring(string):
    longest = string[0] if len(string) > 0 else ""
    for current_idx in range(1, len(string)):
        even_substring = get_palindromic_substring(string, current_idx, True)
        odd_substring = get_palindromic_substring(string, current_idx, False)
        print(even_substring)
        print(odd_substring)
        if len(even_substring) > len(longest):
            longest = even_substring
        if len(odd_substring) > len(longest):
            longest = odd_substring

    return longest


def get_palindromic_substring(string, current_idx, is_even):
    if is_even:
        left_idx = current_idx - 1
        right_idx = current_idx
    else:
        left_idx = current_idx - 1
        right_idx = current_idx + 1

    while left_idx >= 0 and right_idx < len(string):
        if string[left_idx] == string[right_idx]:
            left_idx = left_idx - 1
            right_idx = right_idx + 1
        else:
            break
    return string[left_idx + 1 : right_idx]


test = "a"
print(longestPalindromicSubstring(test))
