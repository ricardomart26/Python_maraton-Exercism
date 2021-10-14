def flatten(iterable):
    new_list = list()
    for i in iterable:
        if i == 0:
            continue
        if type(i) == list:
            for l in i:
                if l == 0:
	                continue
                new_list.append(l)
        else:
            new_list.append(i)
    return new_list

print(flatten([1,[2,3,0,4],[0],5]))
