def color_code(color):
    if color in ["Black", "black"]:
        return 0
    elif color in ["Brown", "brown"]:
        return 1
    elif color in ["Red", "red"]:
        return 2
    elif color in ["Orange", "orange"]:
        return 3
    elif color in ["Yellow", "yellow"]:
        return 4
    elif color in ["Green", "green"]:
        return 5
    elif color in ["Blue", "blue"]:
        return 6
    elif color in ["Violet", "violet"]:
        return 7
    elif color in ["Grey", "grey"]:
        return 8
    return 9


def colors():
    return     [
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
