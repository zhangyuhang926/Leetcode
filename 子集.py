def subsets(nums):
    res = []
    def dfs(lst, nums, ops):
        res.append(lst[:])
        for i in range(ops, len(nums)):
            lst.append(nums[i])
            dfs(lst, nums, i+1)
            lst.pop()
    dfs([], nums, 0)
    return res

nums = [1, 2, 3]
print(subsets(nums))