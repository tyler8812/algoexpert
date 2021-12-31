def arrayOfProducts(array):
    # Write your code here.
    # O(n^2) time O(n) space
    answer = []
    for i in range(len(array)):
        temp = 1
        for j in range(len(array)):
            if i != j:
                temp *= array[j]

        answer.append(temp)

    return answer
