# -- coding: utf-8 --
"""

Created on: 29/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
competitions = [["HTML", "C#"], ["C#", "python"], ["python", "HTML"]]

results = [0, 0, 1]
comp_0 = []
comp_1 = []

# Prueba sin éxito
def tournament_winner(competitions, results):
    count = 0
    while count < len(competitions):
        for r in range(0, len(results)):
            if r == 0:
                comp_0.append(competitions[1])
            elif r == 1:
                comp_1.append(competitions[0])
        return comp_0, comp_1


print(tournament_winner(competitions, results))


# Prueba sin éxito
def tournament_winner(competitions, results):
    for c in range(0, len(competitions)):
        for r in range(0, len(results)):
            if r == 0:
                comp_0.append(competitions[c][1])
            elif r == 1:
                comp_1.append(competitions[c][0])
    return comp_0, comp_1


print(tournament_winner(competitions, results))