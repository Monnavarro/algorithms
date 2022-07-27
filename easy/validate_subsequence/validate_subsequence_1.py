# -- coding: utf-8 --
"""

Created on: 27/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [5, 1, 22, 22, 25, 6, -1, 8, 10]


def is_valid_subsequence_h(array, sequence):
    idx_list = []

    if len(sequence) > len(array):
        return False

    if len(sequence) == len(array) and sequence != array:
        return False

    for x in sequence:
        try:
            idx_list.append(array.index(x))
            array.remove(x)
        except ValueError:
            return False

    return idx_list == sorted(idx_list, reverse=False)


print(is_valid_subsequence_h(array, sequence))



