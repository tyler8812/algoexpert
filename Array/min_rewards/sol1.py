a = [8, 4, 2, 1, 3, 6, 7, 9, 5]


def minRewards(scores):
    # naive base method O(n^2) time O(n) space
    answer = [0 for i in scores]
    answer[0] = 1

    for i in range(1, len(scores)):

        if scores[i] > scores[i-1]:
            answer[i] = answer[i-1] + 1
        elif scores[i] < scores[i-1]:
            answer[i] = 1
            currentIdx = i
            while currentIdx > 0:
                currentIdx -= 1
                if scores[currentIdx] > scores[currentIdx + 1]:
                    answer[currentIdx] = max(
                        answer[currentIdx], answer[currentIdx + 1] + 1)
                else:
                    break

    return sum(answer)


print(minRewards(a))
