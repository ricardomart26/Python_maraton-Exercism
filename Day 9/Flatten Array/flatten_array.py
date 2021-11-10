def flatten(iterable):
    res = []
    for elem in iterable:
        if type(elem) != list:
            res.append(elem)
        elif type(elem) != None:
            res += flatten(elem)
    return res
