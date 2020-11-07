def threeSumClosest(nums, target):
    n = len(nums)
    if not n or n < 3:
        return 0
    nums.sort()
    res = nums[0] + nums[1] + nums[2]

    for i in range(n-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        L = i + 1
        R = n - 1
        while L < R:
            min_num = nums[i] + nums[L] + nums[L+1]
            if target < min_num:
                if abs(res-target) > abs(min_num-target):
                    res = min_num
                    break
            max_num = nums[i] + nums[R] + nums[R-1]
            if target > max_num:
                if abs(res-target) > abs(max_num-target):
                    res = max_num
                    break
            total = nums[i] + nums[L] + nums[R]
            if total == target:
                return total
            if abs(total-target) < abs(res-target):
                res = total
            if total > target:
                R -= 1
                while L < R and nums[R] == nums[R+1]:
                    R -= 1
            else:
                L += 1
                while L < R and nums[L] == nums[L-1]:
                    L += 1                  
    return res

nums = [-1,2,1,-4]
print(threeSumClosest(nums, 1))