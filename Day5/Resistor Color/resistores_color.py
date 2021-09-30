def color_code(color):
    if color == "Black" or color == "black":
        return 0
    elif color == "Brown" or color == "brown":
        return 1
    elif color == "Red" or color == "red":
        return 2
    elif color == "Orange" or color == "orange":
        return 3
    elif color == "Yellow" or color == "yellow":
        return 4
    elif color == "Green" or color == "green":
        return 5
    elif color == "Blue" or color == "blue":
        return 6
    elif color == "Violet" or color == "violet":
        return 7
    elif color == "Grey" or color == "grey":
        return 8
    return 9


def colors():
    list = [
    "black",
    "brown", 
    "red", 
    "orange", 
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]
    return list
