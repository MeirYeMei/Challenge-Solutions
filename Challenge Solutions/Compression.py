def f(text):
    count = 0
    sub = ""
    num = ""
    res = ""
    iscom = False
    for c in text:
        #print(c)
        if ord(c) >= ord('0') and ord(c) <= ord('9'):
            num += c

        elif c == '[':
            iscom = True
            if count != 0:
                sub +=c
            count += 1

        elif c == ']':
            count -= 1
            if count == 0:
                res += int(num) * f(sub)
                sub = ""
                num = ""

            else:
                sub += c
        else:
            sub += c

    if not iscom:
        res = sub
        sub = ""
    return res + sub

print(f("3[abc]4[ab]c"))
