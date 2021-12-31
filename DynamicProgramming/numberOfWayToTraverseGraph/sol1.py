# 巴斯卡定理
# O(n+m) time O(1) sapce
def numberOfWaysToTraverseGraph(width, height):
    total = width + height - 2
    answer = 1
    for i in range(1, total+1):
        answer *= i
    for i in range(1, width):
        answer /= i
    for i in range(1, height):
        answer /= i
    return answer
