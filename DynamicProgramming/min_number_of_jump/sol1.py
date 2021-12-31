# O(n^2) time O(n) space
def minNumberOfJumps(array):
    jump = [float("inf") for _ in range(len(array))]
    jump[0] = 0

    for i in range(1, len(array)):
        for j in range(0, i):
            if array[j] >= i - j:
                jump[i] = min(jump[j] + 1, jump[i])

        print(jump)
    return jump[-1]


minNumberOfJumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3])
