# -- coding: utf-8 --
"""

Created on: 28/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
def sorted_square_array(array):
    sorted_squares = [0 for _ in array]

    for idx in range(len(array)):
        value = array[idx]
        sorted_squares[idx] = value * value


    sorted_squares.sort()
    return sorted_squares

array = [-50, -13, -2, -1, 0, 0, 1, 1, 2, 3, 19, 20]

print(sorted_square_array(array))