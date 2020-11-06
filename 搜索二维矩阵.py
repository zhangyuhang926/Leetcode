def searchMatrix(matrix, target):
    m = len(matrix)
    if m == 0:
        return False

    n = len(matrix[0])

    left = 0
    right = m * n - 1

    while left <= right:
        pivote_index = (left + right) // 2
        pivote_element = matrix[pivote_index//n][pivote_index%n]

        if pivote_element == target:
            return True
        else:
            if target < pivote_element:
                right -= 1
            else:
                left += 1

    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
target = 3
print(searchMatrix(matrix, target))