# -- coding: utf-8 --
"""

Created on: 28/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""

def sorted_squared_array(array):
    array_squared = []
    for n in array:
        array_squared.append((n * n))
        array_squared = sorted(array_squared, reverse=False)
    return array_squared


array = [-2, -1]

print(sorted_squared_array(array))
