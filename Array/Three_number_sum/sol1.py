def threeNumberSum(array, targetSum):
    # Write your code here.
    # O(n^3) time 	O(n) space
    output = []
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            for k in range(j+1, len(array)):
                # print(array[i], array[j])
                # print(targetSum)
                if (array[i] + array[j] + array[k]) == targetSum:
                    output.append([array[i], array[j], array[k]])

    if len(output) < 1:
        return []
    else:
        for i in output:
            i.sort()
        output.sort()
        return output
