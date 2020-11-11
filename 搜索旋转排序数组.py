def search(nums, target):
    n = len(nums)
    if n == 0:
        return -1

    left = 0
    right = n - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            if nums[mid] <= target and target <= nums[right]:
                left = mid
            else:
                right = mid - 1
        else:
            if nums[left] <= target and target <= nums[mid-1]:
                right = mid -1
            else:
                left = mid
        if nums[left] == target:
            return left
    return -1

nums = [4,5,6,7,0,1,2]
print(search(nums, 0))