class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find the row to search in

        # possible to filter by checking the last elem of the row and seeing if > target?

        left, right, row = 0, len(matrix[0]) - 1, 0

        for i in range(len(matrix)):
            if matrix[i][right] >= target:
                if matrix[i][right] == target:
                    return True
                row = i
                break
        
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False