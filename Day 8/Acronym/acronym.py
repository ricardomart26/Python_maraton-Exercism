def abbreviate(words):
    splited = words.split()
    new_splited = list()
    for i in splited:
        if "-" in i:
            new_splited.extend(i.split("-"))
            continue
        elif "_" in i:
            new_splited.extend(i.split("_"))
        else:
            new_splited.append(i)
    return "".join(i[:1].upper() for i in new_splited)
