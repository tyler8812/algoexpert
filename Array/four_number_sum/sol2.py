def fourNumberSum(array, targetSum):
    # worst:O(n^3) avg:O(n^3)time O(n^2) space
    # using hashTable for every two sum
    answer = []
    hashtable = {}
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            currentKey = array[i] + array[j]
            targetInHash = targetSum - currentKey
            if targetInHash in hashtable:
                for pair in hashtable[targetInHash]:
                    answer.append(pair + [array[i], array[j]])

        for k in range(0, i):
            currentKey = array[k] + array[i]
            if currentKey not in hashtable:
                hashtable[currentKey] = [[array[k], array[i]]]
            else:
                hashtable[currentKey].append([array[k], array[i]])

    return answer
