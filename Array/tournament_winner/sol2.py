def tournamentWinner(competitions, results):
    # Write your code here.
    # add every to score then sort it.
    # O(nlog(n)) time O(k) space.
    # n is competitions number, k is total teams.
    scores = {}
    for i in range(len(competitions)):
        if results[i] == 0:
            updateScore(competitions[i][1], 3, scores)
        elif results[i] == 1:
            updateScore(competitions[i][0], 3, scores)
        else:
            print("`somethings wrong")

    ans = sorted(scores.items(), key=lambda x: x[1], reverse=True)[0][0]
    return ans


def updateScore(team, points, scores):
    if team not in scores:
        scores[team] = 0
    scores[team] += points
