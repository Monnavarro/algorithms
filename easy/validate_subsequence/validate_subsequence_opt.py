# -- coding: utf-8 --
"""

Created on: 27/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
# otra solución
def is_valid_subsequence(array, sequence):
    seq_idx = 0
    for value in array:
        if seq_idx == len(sequence):
            break
        if sequence[seq_idx] == value:
            seq_idx += 1
        return seq_idx == len(sequence)


array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [5, 1, 22, 22, 25, 6, -1, 8, 10]

print(is_valid_subsequence(array, sequence))
