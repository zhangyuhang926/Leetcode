def reverse(n):
    if -10 < n < 10:
        return n

    str_n = str(n)
    if str_n[0] != '-':
        str_n = str_n[::-1]
        n = int(str_n)
    else:
        str_n = str_n[:0:-1]
        n = int(str_n)
        n = -n
    return n if -2147483648 < n < 2147483647 else 0

print(reverse(-256))