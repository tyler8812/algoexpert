def threeNumberSum(array, targetSum):
    # Write your code here.
    # O(n^2) time O(n) space
    array.sort()
    output = []
    for i in range(0, len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while(left < right):
            if (array[i] + array[left] + array[right]) == targetSum:
                output.append([array[i], array[left], array[right]])
                # important
                left += 1
                right -= 1
            elif (array[i] + array[left] + array[right]) < targetSum:
                left += 1
            elif (array[i] + array[left] + array[right]) > targetSum:
                right -= 1
            else:
                print('error')
                return 0
    return output
