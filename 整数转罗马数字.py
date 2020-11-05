def intToRoman(num):
    nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romans = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

    index = 0
    res = ''

    while index < len(nums):
        if num >= nums[index]:
            res += romans[index]
            num -= nums[index]
        index += 1
    return res

print(intToRoman(1994))