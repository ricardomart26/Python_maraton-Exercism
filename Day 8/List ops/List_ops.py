def append(list1, list2):
    return list1 + list2


def concat(lists):
    new_list = list()
    for i in lists:
        new_list.extend(i)
    return new_list


def filter(function, list):
    return [i for i in list if function(i) == True]


def length(list):
    return len(list)


def map(function, list):
    ret = []
    for i in list:
        ret.append(function(i))
    return ret

def foldl(function, list, initial):
    accumulator = initial
    if not len(list):
        return initial
    for i in list:
        accumulator = function(initial, i)
    return accumulator + initial


def foldr(function, list, initial):
    if not len(list):
        return initial

def reverse(list):
    return list[::-1]
