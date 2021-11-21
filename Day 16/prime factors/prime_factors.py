def factors(value):
    res = []
    divisor = 2
    while(value != 1):
        if value % divisor == 0:
            value /= divisor
            res.append(divisor)
        else:
            divisor += 1
    return res

