
# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 0

def check_equality(sublist, superlist, len_sup, ret):
    if sublist[0] not in superlist:
        return UNEQUAL
    index = superlist.index(sublist[0])
    size = len(sublist)
    j = 0
    for i in range(len_sup):
        if superlist[index + i] == sublist[j]:
            j += 1
            if size - i == j:
                return ret
        elif sublist[0] in superlist[index+i:]:
            index = superlist.index(sublist[0], index + i)
        else:
            break
        if index + i >= size:
            return ret
    return UNEQUAL
        
def sublist(list_one, list_two):
    one_size = len(list_one)
    two_size = len(list_two)
    if not one_size and not two_size:
        return EQUAL
    elif not one_size:
        return SUBLIST
    elif not two_size:
        return SUPERLIST
    if one_size == two_size:
        if list_one == list_two:
            return EQUAL
        else:
            return 0
    elif one_size > two_size:
        return check_equality(list_two, list_one, one_size, SUPERLIST)                
    else:
        return check_equality(list_one, list_two, two_size, SUBLIST)
