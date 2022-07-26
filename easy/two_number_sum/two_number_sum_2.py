# -- coding: utf-8 --
"""

Created on: 26/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
def two_number_sum(array, target_sum):
    array.sort()
    left = 0
    right = len(array) -1
    while left < right:
        current_sum = array[left] + array[right]
        if current_sum == target_sum:
            return [array[left], array[right]]
        elif current_sum < target_sum:
            left += 1
        elif current_sum > target_sum:
            right -= 1
    return []


print(two_number_sum([-1, 10, 15, -4, 5, 0, 4], -5))

