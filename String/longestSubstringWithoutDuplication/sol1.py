# O(n) time | O(min(n, a)) space
# n: chars of string, a: appear of char
def longestSubstringWithoutDuplication(string):
    longest = [0, 1]
    start_idx = 0
    char_appear = {}
    for i, char in enumerate(string):
        if char in char_appear:
            print(char, char_appear[char])
            start_idx = max(start_idx, char_appear[char] + 1)
        if longest[1] - longest[0] < i - start_idx + 1:
            longest = [start_idx, i + 1]
        print(i, start_idx)
        print(char_appear)
        print(longest)
        char_appear[char] = i
    print(string[longest[0] : longest[1]])
    return string[longest[0] : longest[1]]


test = "clementisaczap"
longestSubstringWithoutDuplication(test)
