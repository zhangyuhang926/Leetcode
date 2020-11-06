def longestCommonPrefix(strs):
    if not strs:
        return ""

    prefix, count = strs[0], len(strs)
    for i in range(1, count):
        prefix = lcp(prefix, strs[i])
        if not prefix:
            break
    return prefix

def lcp(str1, str2):
    length, index = min(len(str1), len(str2)), 0
    while index < length and str1[index] == str2[index]:
        index += 1
    return str1[:index]

strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))