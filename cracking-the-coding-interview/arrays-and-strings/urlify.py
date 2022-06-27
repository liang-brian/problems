def urlify(s):
    n = len(s) - 1

    l = n
    r = n
    fill = True

    while l >= 0:
        if fill:
            if s[l] != ' ':
                fill = False
            else:
                l -= 1
        else:
            if s[l] == ' ':
                s[r] = '0'
                s[r - 1] = '2'
                s[r - 2] = '%'
                r -= 3
            else:
                s[r] = s[l]
                r -= 1
            l -= 1
    
    return s

print(urlify(list('Mr John Smith    ')))
