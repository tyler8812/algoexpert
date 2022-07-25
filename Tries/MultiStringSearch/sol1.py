# O(n) space (output of the small strings with boolean)
# O(bns) time
# n: length of the small strings
# b: length of big string
# s: length of the biggest small string

# O(b * n * s)
def multiStringSearch(bigString, smallStrings):
    return [is_in_big_string(bigString, small_string) for small_string in smallStrings]


# O(b * s)
def is_in_big_string(big_string, small_string):
    for i in range(len(big_string)):
        if is_in_big_string_helper(big_string, small_string, i):
            return True
    return False


# O(s) time
def is_in_big_string_helper(big_string, small_string, start_idx):
    if start_idx + len(small_string) > len(big_string):
        return False
    for i in range(len(small_string)):
        if small_string[i] != big_string[start_idx + i]:
            return False

    return True


big_string = "this is a big string"
small_strings = ["this", "yo", "is", "a", "bigger", "string", "kappa"]
print(is_in_big_string(big_string, "yo"))
