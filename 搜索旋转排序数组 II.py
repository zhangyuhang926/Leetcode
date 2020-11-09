def search(nums, target):
    n = len(nums)
    if n == 0:
        return False

    left = 0
    right = n - 1
    while left <= right:
        mid = left + (right - left + 1) // 2
        if nums[left] == nums[mid] == nums[right]:
            left -= 1
            right += 1

        if nums[mid] == target:
            return True
        elif nums[left] < nums[mid]:
            if nums[left] <= target < nums[mid]:
                right -= 1
            else:
                left += 1
        else:
            if nums[mid] < target <= nums[right]:
                left += 1
            else:
                right -= 1
    return False

nums = [2,5,6,0,0,1,2]
print(search(nums, 0))