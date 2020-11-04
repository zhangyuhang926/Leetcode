def longestPalindrome(s):
    size = len(s)
    if size < 2:
        return size

    dp = [[False for _ in range(size)] for _ in range(size)]

    max_len = 1
    start = 0

    for j in range(1, size):
        for i in range(0, j):
            if s[j] == s[i]:
                if j-i < 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = False

            if dp[i][j]:
                cur_len = j-i+1
                if cur_len > max_len:
                    max_len = cur_len
                    start = i
    return s[start:start+max_len]

s = 'babad'
print(longestPalindrome(s))