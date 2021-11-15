import math
import unittest

def find(search_list, value):
    lower = 0
    size = len(search_list)
    heigher = size - 1
    if search_list is [] or value not in search_list:
        raise ValueError("not found.")
    while (True):
        middle = math.floor((lower + heigher) / 2)
        if search_list[middle] == value:
            return middle
        elif search_list[middle] > value and middle != 0:
            if lower == heigher:
                break;
            heigher = middle - 1
        elif search_list[middle] < value and middle != 0:
            if lower == heigher:
                break;
            lower = middle + 1
    raise ValueError("not found.")

print(find([1, 3, 4, 6, 8, 9, 11], 7))
