class Solution(object):
    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        colums = len(matrix[0])
        
        low = 0
        high = (rows * colums) - 1

        while low <= high:
            mid = (low + high) // 2
            row = mid // colums
            col = mid % colums
            value = matrix[row][col]

            if value == target:
                return True
            elif value < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False
            