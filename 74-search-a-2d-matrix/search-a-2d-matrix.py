class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        left = 0
        right = len(matrix[row]) - 1
        while row < len(matrix) and target > matrix[row][right]:
            row += 1
        if row >= len(matrix):
            return False
        while left <= right:
            middle = (left + right) // 2
            if target == matrix[row][middle]:
                return True
            elif target > matrix[row][middle]:
                left = middle + 1
            else:
                right = middle - 1
        return False