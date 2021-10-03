import math

def find(search_list, value):
    while (True):
        size = len(search_list)
        middle = math.floor(size / 2)
        if search_list[middle] == value:
            return middle
        elif search_list[middle] > value:
            search_list = search_list[:middle]
        elif search_list[middle] < value:
            search_list = search_list[middle:]
        else:
            return "Not found."

print(find([1, 2, 3, 4, 5, 6, 8], 1))
