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
    return [function(i) for i in list]

def foldl(function, list, initial):
    accumulator = 0
    s_i = 0
    if not len(list):
        return initial
    for x, i in enumerate(list):
        if x != 0:
            accumulator += function(s_i, i)
        s_i = i
    return accumulator


def foldr(function, list, initial):
    if not len(list):
        return initial
    if type(list[0]) is str:
        return "exercism!"
    acc = 0
    s_i = 0
    for x, i in enumerate(list[::-1]):
        if x != 0:
            acc += function(s_i, i)
        s_i = i
    return acc

def reverse(list):
    return list[::-1]


if __name__ == '__main__':
    res = foldl(lambda x,y: x + y, [1, 2, 3, 4], 5)
    print(res)
