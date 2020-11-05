def maxArea(height):
    max_area = 0
    left = 0
    right = len(height) - 1

    while left < right:
        if height[left] < height[right]:
            max_area = max(max_area, height[left] * (right - left))
            left += 1
        else:
            max_area = max(max_area, height[right] * (right - left))
            right -= 1
    return max_area

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))