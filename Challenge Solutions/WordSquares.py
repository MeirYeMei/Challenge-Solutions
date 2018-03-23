def sol1(words):
    length = len(words)
    for row in range(length):
        for col in range(row + 1, length):
                if words[row][col] != words[col][row]:
                    return False

    return True

def sol2(words):
    length = len(words[0])
    mp = {}
    for word in words:
        for i in range(length):
            if (word[i], i) not in mp:
                mp[(word[i], i)] = set()

            mp[(word[i], i)].add((word))

    res = set()
    for key in mp:
        if key[1] == 0:
            for word in mp[key]:
                res.add((word,))
    ret = []
    while res:
        current = res.pop()
        keys = [(current[i][len(current)], i) for i in range(len(current))]
        candidates = []
        for key in keys:
            if key in mp:
                candidates.append(mp[key])
            else:
                candidates.append(set())

        if len(candidates) != 0:
            for valid in set.intersection(*candidates):
                current += (valid, )
                if len(current) == length:
                    ret.append(current)
                else:
                    res.add(current)

    return ret

words = ["AREA", "BALL", "DEAR", "LADY", "LEAD", "YARD"]
print(sol2(words))
