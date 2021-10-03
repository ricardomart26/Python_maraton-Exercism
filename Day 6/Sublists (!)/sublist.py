"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 0

def check_equality(sublist, superlist, len_sup, ret):
    check = [superlist.index(num) for num in sublist]
    if check == -1:
        return UNEQUAL
    index = superlist.index(sublist[0])
    size = len(sublist)
    j = 0
    if index == -1:
        return 0
    for i in range(len_sup):
        if superlist[index + i] == sublist[j]:
            j += 1
            if size == j:
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
