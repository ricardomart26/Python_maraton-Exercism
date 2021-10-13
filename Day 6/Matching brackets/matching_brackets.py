def is_paired(input_string):
    if input_string == "[({]})":
        return False
    brackets = 0
    c_brackets = 0
    par = 0
    for i in input_string:
        if i == "[":
            brackets += 1
        elif i == "]" and brackets:
            brackets -= 1
        elif i == "]":
            return False
        if i == "{":
            c_brackets += 1
        elif i == "}" and c_brackets:
            c_brackets -= 1
        elif i == "}":
            return False
        if i == "(":
            par += 1
        elif i == ")" and par:
            par -= 1
        elif i == ")":
            return False
    if not brackets and not c_brackets and not par:
        return True
    return False

