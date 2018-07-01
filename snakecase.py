def to_underscore(string):
    s = string
    the_len = len(string)

    for i in string:
        x = string.index(i)-1
        num = x % len(string)
        if string[x+1].upper() == i:
            if num + 1 != len(string):
                s = s[:s.index(i)] + "_" + s[s.index(i):]


    string = string.lower()

to_underscore('TestController')