# -- coding: utf-8 --
"""

Created on: 1/8/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
coins = [1, 2, 5]


def non_constructible_change(coins):
    coins.sort()
    minimum_change = 0
    for coin in coins:
        if coin > minimum_change + 1:
            break
        minimum_change += coin
    return minimum_change + 1

print(non_constructible_change(coins))



