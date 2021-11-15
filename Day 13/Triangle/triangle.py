def equilateral(sides):
    save_i = None
    for i in sides:
        if save_i not in [None, i] or i <= 0:
            return False
        save_i = i
    return True

def isosceles(sides):
    if equilateral(sides):
        return True
    for i in sides:
        if i <= 0:
            return False
    for i in sides:
        count = 0
        sum = 0
        for x in sides:
            if i == x:
                count += 1
                sum += x
            else:
                diff = x
        if count >= 2 and sum >= diff:
            return True
    return False

def scalene(sides):
    if equilateral(sides) or isosceles(sides):
        return False
    diff = sum(sides) - max(sides)
    return diff > max(sides)
