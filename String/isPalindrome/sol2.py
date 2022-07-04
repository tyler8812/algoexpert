# O(n) time | O(n) space
# recursive
def isPalindrome(string, current_first=0):
    current_last = len(string) - 1 - current_first
    return (
        True
        if current_first >= current_last
        else string[current_first] == string[current_last]
        and isPalindrome(string, current_first + 1)
    )
