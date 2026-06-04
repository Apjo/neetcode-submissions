class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        low, hi = 0, cols - 1
        while low <= rows - 1 and hi >= 0:
            if matrix[low][hi] == target:
                return True
            elif matrix[low][hi] < target:
                low +=1
            else:
                hi-=1
        return False
