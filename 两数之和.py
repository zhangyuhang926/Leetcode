def twoSum(nums, target):
    hashmap = {}
    for ind, num in enumerate(nums):
        hashmap[num] = ind
    for i, num in enumerate(nums):
        j = hashmap.get(target - num)
        if j is not None and j != i:
            return [i, j]

nums = [2, 7, 11, 15]
print(twoSum(nums, 9))