# O(n) time | O(n) space
# reversed string
def isPalindrome(string):
    reversed_string = []
    for i in reversed(range(len(string))):
        reversed_string.append(string[i])
    return string == "".join(reversed_string)


string = "abcdcba"
print(isPalindrome(string))
