# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.

# O(n) time | O(d) space
# n is the length of array, includeing sub-element
# d is the greatest depth of special array (recursive)
def productSum(array, depth=1):
    sum = 0
    for value in array:
        if type(value) == list:
            sum += productSum(value, depth=depth + 1)
        else:
            sum += value

    return sum * depth
