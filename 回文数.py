def isPalindrome(x):
    if x < 0:
        return False

    ans = 0
    old = x
    while x > 0:
        tmp = x%10
        ans = ans*10 + tmp
        x //= 10
    return ans == old

print(isPalindrome(121))