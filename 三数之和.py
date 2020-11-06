def threeSum(nums):
    n = len(nums)
    if n < 3:
        return []

    nums.sort()
    res = []

    for i in range(n-2):
        if nums[i] > 0 or nums[-1] < 0:
            break
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left = i + 1
        right = n - 1
        while left < right:
            num = nums[i] + nums[left] + nums[right]
            if num == 0:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -=1
            elif num < 0:
                left += 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
            else:
                right -= 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1
    return res

nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))