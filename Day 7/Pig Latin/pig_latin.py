def isvowel(c):
    if (c in 'AEIOUYaeiouy'):
        return True
    return False

def cmp(str, str2, len):
    for i in range(len):
        if str[i] != str2[i]:
            return (0)
    return (1)

def translate(text):
    if " " in text:
        return " ".join(translate(i) for i in text.split())
    elif cmp(text, "xr", 2) or cmp(text, "yt", 2):
        return text + 'ay'
    index = 0
    for c in text:
        if isvowel(c) is False or (c == 'y' and text[0] == 'y'):
            index += 1
        elif text[index - 1] is 'q' and c is 'u':
            index += 1
        else:
            return text[index:] + text[:index] + 'ay'
