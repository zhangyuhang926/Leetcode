def combine(n, k):
    res, path = [], []
    if k == 0 or k > n:
        return res

    dfs(n, k, 1, path, res)
    return res


def dfs(n, k, beg, path, res):
    if len(path) == k:
        res.append(path[:])
    for i in range(beg, n+1):
        path.append(i)
        dfs(n, k, i+1, path, res)
        path.pop()


print(combine(4, 2))