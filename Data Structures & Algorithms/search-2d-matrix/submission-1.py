class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        matrix_len = rows * cols - 1
        low, hi = 0, matrix_len
        while low <= hi:
            mid = (low + hi) // 2
            row_loc = mid // cols
            col_loc = mid % cols
            if matrix[row_loc][col_loc] == target:
                return True
            elif matrix[row_loc][col_loc] <= target:
                low = mid + 1
            else:
                hi = mid - 1
        return False
        