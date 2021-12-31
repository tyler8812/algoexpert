HOME_TEAM_WON = 1


def tournamentWinner(competitions, results):
    # Write your code here.
    # add every to score then sort it.
    # O(n) time O(k) space
    highest = ""
    scores = {highest: 0}
    for idx, competition in enumerate(competitions):
        result = results[idx]
        homeTeam, awayTeam = competition

        winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam

        updateScore(winningTeam, 3, scores)

        if scores[highest] < scores[winningTeam]:
            highest = winningTeam

    return highest


def updateScore(team, points, scores):
    if team not in scores:
        scores[team] = 0
    scores[team] += points
