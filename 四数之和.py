def fourSum(nums, target):
    n = len(nums)
    if n < 4:
        return []
    nums.sort()
    res = []

    for i in range(n-3):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, n-2):
            if nums[j] == nums[j-1] and j-1 != i:
                continue
            left = j + 1
            right = n - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total < target:
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                elif total > target:
                    right -= 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                else:
                    res.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
    return res

nums = [1, 0, -1, 0, -2, 2]
print(fourSum(nums, 0))