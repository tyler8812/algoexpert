

def minRewards(scores):
    # Write your code here.
    # find local min and expand from the local min
    # O(n) time O(n) space
    rewards = [1 for _ in scores]
    local_min = getLocalMin(scores)
    for local_min_idx in local_min:
        expandFromLocalMinIdx(local_min_idx, scores, rewards)
    return sum(rewards)


# find local min
def getLocalMin(scores):
    if len(scores) == 1:
        return [0]
    localMins = []
    for i in range(len(scores)):
        if i == 0 and scores[i+1] > scores[i]:
            localMins.append(i)
        elif i == len(scores) - 1 and scores[i-1] > scores[i]:
            localMins.append(i)
        elif scores[i-1] > scores[i] and scores[i+1] > scores[i]:
            localMins.append(i)
    return localMins

# 延伸local min 到兩邊的最大值


def expandFromLocalMinIdx(idx, scores, rewards):
    leftIdx = idx - 1
    while leftIdx >= 0 and scores[leftIdx] > scores[leftIdx + 1]:
        rewards[leftIdx] = max(rewards[leftIdx], rewards[leftIdx + 1] + 1)
        leftIdx -= 1
    rightIdx = idx + 1
    while rightIdx < len(scores) and scores[rightIdx] > scores[rightIdx - 1]:
        rewards[rightIdx] = max(rewards[rightIdx], rewards[rightIdx - 1] + 1)
        rightIdx += 1
