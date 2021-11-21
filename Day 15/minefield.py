def put_dots_to_zero(mines):
    new = ""
    for elem in mines:
        for i in elem:
            new += '0' if i == ' ' else (i)
    return new
            

def annotate(minefield):
    if minefield:
        minefield = put_dots_to_zero(minefield)
        print(minefield)
    pass

print(annotate([" * ", " *  * "]))
