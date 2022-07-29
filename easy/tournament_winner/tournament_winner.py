# -- coding: utf-8 --
"""

Created on: 29/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""

competitions: [
    ["HTML", "Java"],
    ["Java", "Python"],
    ["Python", "HTML"]
  ]
results: [0, 1, 1]

HOME_TEAM_WON = 1

def tournament_winner(competitions, results):
    current_best_team = ""
    scores = {current_best_team: 0}

    for idx, competition in enumerate(competitions):
        result = results[idx]
        home_team, away_team = competition

        wining_team = home_team if result == HOME_TEAM_WON else away_team

        update_scores(wining_team, 3, scores)

        if scores[wining_team] > scores[current_best_team]:
            current_best_team = wining_team

    return current_best_team

def update_scores(team, points, scores):
    if team not in scores:
        scores[team] = 0

    scores[team] += points



print(tournament_winner(competitions, results))
