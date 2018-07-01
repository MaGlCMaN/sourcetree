def to_underscore(string):
    s = string
    the_len = len(string)

    for i in string:
        x = string.index(i)-1
        num = x % len(string)
        if string[x+1].upper() == i:
            if num + 1 != len(string):
                try:
                    z = int(i)
                    z += 0
                    n = num + 2
                    s = s[:n] + "_" + s[n:]
                except ValueError:
                    s = s[:s.index(i)] + "_" + s[s.index(i):]


    s = s.lower()
    return s

to_underscore('TestController')