def myAtoi(s):
    i = 0
    n = len(s)

    while i<n and s[i] == ' ':
        i += 1
    if n == 0 or i == n:
        return 0

    flag = 1
    if s[i] == '-':
        flag = -1
    if s[i] == '+' or s[i] == '-':
        i += 1

    INT_MAX = 2**31-1
    INT_MIN = -2**31
    ans = 0
    while i < n and '0' < s[i] < '9':
        ans = ans*10 + int(s[i]) - int('0')
        i += 1
        if ans > INT_MAX:
            break

    ans = ans * flag
    if ans > INT_MAX:
        return INT_MAX

    return INT_MIN if ans < INT_MIN else ans

print(myAtoi('-34'))