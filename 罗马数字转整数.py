def romanToInt(s):
    roma = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}

    n = len(s)
    count = 0

    for i in range(n-1):
        if roma[s[i]] < roma[s[i+1]]:
            count -= roma[s[i]]
        else:
            count += roma[s[i]]
    count += roma[s[-1]]
    return count

s = "LVIII"
print(romanToInt(s))