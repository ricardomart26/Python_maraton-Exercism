def encode(plain_text):
    helper = 0
    alpha = "abcdefghijklmnopqrstuvwxyz"
    ret = ""
    i = 0
    for c in plain_text.lower():
        helper = alpha.find(c)
        if helper == -1:
            if c not in [' ', ',', '.']:
                ret += c
            else:
                continue
        else:
            ret += alpha[-helper - 1]
        i += 1
        if i % 5 == 0:
            ret += ' '
    if i % 5 == 0:
        return (ret[:-1])
    return ret


def decode(ciphered_text):
    helper = 0
    alpha = "abcdefghijklmnopqrstuvwxyz"
    ret = ""
    for c in ciphered_text.lower():
        helper = alpha.find(c)
        if helper == -1:
            if c not in [' ', ',', '.']:
                ret += c
        else:
            ret += alpha[-helper - 1]
    return ret
