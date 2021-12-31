def tournamentWinner(competitions, results):
    # Write your code here.
    # add every to score then sort it.
    # O(n) time O(k) space
    highest = ""
    highestScore = 0
    scores = {}
    for i in range(len(competitions)):
        if results[i] == 0:
            updateScore(competitions[i][1], 3, scores)
            if scores[competitions[i][1]] >= highestScore:
                highest = competitions[i][1]
                highestScore = scores[competitions[i][1]]
        elif results[i] == 1:
            updateScore(competitions[i][0], 3, scores)
            if scores[competitions[i][0]] >= highestScore:
                highest = competitions[i][0]
                highestScore = scores[competitions[i][0]]
        else:
            print("`somethings wrong")

    return highest


def updateScore(team, points, scores):
    if team not in scores:
        scores[team] = 0
    scores[team] += points
