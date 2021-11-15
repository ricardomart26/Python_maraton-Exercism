def convert(number):
    if number % 3 and number % 5 and number % 7:
        return str(number)
    ret = ""
    if number % 3 == 0:
        ret += "Pling"
    if number % 5 == 0:
        ret += "Plang"
    if number % 7 == 0:
        ret += "Plong"
    return ret
