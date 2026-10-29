class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        M,N = len(matrix), len(matrix[0])
        #transpose
        for i in range(M):
            for j in range(i, N):
                matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]
        print(f"after transpose={matrix}")
        #reverse each row
        def rev(row):
            lo, hi=0, N - 1
            while lo < hi:
                matrix[row][lo], matrix[row][hi] = matrix[row][hi], matrix[row][lo]
                lo+=1
                hi-=1
        for i in range(M):
            rev(i)