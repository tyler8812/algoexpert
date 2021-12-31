
def minRewards(scores):

    # 從左到右判斷 再從右到左判斷
    # 這樣可以找到從左到右 網上的reward和從右到左往上的reward
    # 這樣就不用找local min
    # O(n) time O(n) space
    rewards = [1 for _ in scores]

    for i in range(1, len(scores)):

        if scores[i] > scores[i - 1]:
            rewards[i] = rewards[i - 1] + 1

    for i in reversed(range(0, len(scores)-1)):

        if scores[i] > scores[i + 1]:
            rewards[i] = max(rewards[i], rewards[i+1] + 1)

    return sum(rewards)
