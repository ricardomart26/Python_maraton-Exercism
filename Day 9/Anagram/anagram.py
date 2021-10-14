def find_anagrams(word, candidates):
    ret = list()
    size = len(word) - 1
    word = word.lower()
    for i in candidates:
        i_low = i.lower()
        if len(i) != len(word) or i_low == word:
            continue
        for j in range(len(word)):
            if word[j] not in i_low:
                break
            else:
                x = 0
                while x < len(i_low) - 1:
                    if word[j] == i_low[x]:
                        if x == 0:
                            i_low = i_low[1:]
                        else:
                            i_low = i_low[:x] + i_low[x:] 
                    x += 1
        if j == len(word) - 1:
            ret.append(i)
    return ret

candidates = ["stream", "pigeon", "maters"]

print(find_anagrams("master", candidates))

candidates = ["Eons", "ONES"]
print(find_anagrams("nose", candidates))

candidates = ["patter"]
print(find_anagrams("tapper", candidates))

