# -- coding: utf-8 --
"""

Created on: 27/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
# Prueba y error
def is_valid_subsequence(array, sequence):
    count = 0
    while count < len(array):
        if sequence in array:
            return True
        elif sequence == array:
            return True
        else:
            return False
        count += 1

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = []
print(is_valid_subsequence(array, sequence))

def is_valid_subsequence(array, sequence):
    count = 0
    seq = set()
    while count < len(array):
        for n in range(0, len(sequence)):
            if sequence[n] in array:
                seq.add(sequence[n])
                count += 1
        sequence = sorted(sequence)
        print(sequence)
        seq = sorted(list(seq))
        print(seq)
        if sequence == seq:
            return True


def is_valid_subsequence(array, sequence):
    count = 0
    seq = set()
    while count < len(array):
        for n in range(0, len(sequence)):
            if sequence[n] in array:
                seq.add(sequence[n])
                count += 1
        sequence = sorted(sequence)
        seq = sorted(list(seq))
        if sequence == seq:
            return True
        else:
            return False