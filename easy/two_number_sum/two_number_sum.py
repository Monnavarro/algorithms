# -- coding: utf-8 --
"""

Created on: 26/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
array =[3, 5, -4, 8, 11, 1, -1, 6]
target_sum = 21

def two_numer_sum(array, target_sum):
    for n in range(0, len(array)):
        for m in range(0, len(array)):
            if array[n] != array[m] and array[n] + array[m] == target_sum:
                return [array[n], array[m]]
    return []


print(two_numer_sum(array, target_sum))
