# O(n) time | O(1) space
# two pointer
def isPalindrome(string):
    first_idx = 0
    last_idx = len(string) - 1
    while first_idx <= last_idx:
        if string[first_idx] == string[last_idx]:
            first_idx += 1
            last_idx -= 1
        else:
            return False
    return True
