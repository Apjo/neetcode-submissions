class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        M,N = len(matrix), len(matrix[0])
        row_zero, col_zero = False, False
        #determine if a 0 exists on row 0
        for i in range(N):
            if matrix[0][i] == 0:
                row_zero=True
                break

        #determine if a 0 exists on col 0
        for i in range(M):
            if matrix[i][0] == 0:
                col_zero=True
                break
        #iterate from row/col=1 and determine if there is a 0 anywhere, if there is, then mark the row 0 col=j, and row=i col=0 as 0
        for i in range(1, M):
            for j in range(1, N):
                if matrix[i][j] == 0:
                    matrix[0][j]=0
                    matrix[i][0]=0
        #again iterate from row/col=1 and for all matrix[i][0]=0 or matrix[0][j]=0 set those locations matrix[i][j] to 0
        for i in range(1, M):
            for j in range(1, N):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j]=0
        #if there was a 0 seen on row=0 set all cols for row=0 0
        if row_zero:
            for i in range(N):
                matrix[0][i]=0
        #if there was a 0 seen on col=0 set all rows for col=0 0
        if col_zero:
            for i in range(M):
                matrix[i][0]=0

        