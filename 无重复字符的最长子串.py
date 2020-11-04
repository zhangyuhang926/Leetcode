def lengthOfLongestSubstring(s):
    occ = set()

    if not s:
        return 0
    n = len(s)
    rk, ans = -1, 0

    for i in range(n):
        if i != 0:
            occ.remove(s[i-1])
        while rk+1 < n and s[rk+1] not in occ:
            occ.add(s[rk+1])
            rk += 1
        ans = max(ans, rk-i+1)
    return ans

s = 'abcabcbb'
print(lengthOfLongestSubstring(s))