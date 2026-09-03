class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left = 0
        right = (rows * cols) - 1

        while left <= right:
            mid = left + (right - left) // 2
            i, j = int(mid / cols), mid % cols
            if matrix[i][j] == target:
                return True

            elif matrix[i][j] < target:
                left = mid + 1
            
            else:
                right = mid - 1

        return False