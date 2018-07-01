#https://www.codewars.com/kata/convert-pascalcase-string-into-snake-case/train/python

def to_underscore(string):
    s = string
    if s == str(s):
        the_len = len(string)

        for i in string:
            x = string.index(i) - 1
            num = x % len(string)
            if string[x + 1].upper() == i:
                if num + 1 != len(string):
                    try:
                        z = int(i)
                        z += 0
                        n = num + 2
                        s = s[:n] + "_" + s[n:]
                    except ValueError:
                        s = s[:s.index(i)] + "_" + s[s.index(i):]

        s = s.lower()
        s = list(s)
        for i in s:
            if i == "_":
                indx = s.index(i) + 1
                s[s.index(i)] = "*"
                if s[indx] == "_":
                    del s[indx]

        for i in s:
            if i == "*":
                s[s.index(i)] = "_"

        s = ''.join(s)

    else:
        print("Argument cannot be only a number")

    return str(s)

to_underscore('TestController')