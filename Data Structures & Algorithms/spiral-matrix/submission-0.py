class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        M,N = len(matrix), len(matrix[0])
        total = M * N
        st_col, end_col = 0, N - 1
        st_row, end_row=0, M - 1
        #while the total elements in output != M*N
        while len(res) < total:
            #fill 0th row
            for i in range(st_col, end_col + 1):
                res.append(matrix[st_row][i])
            #goto next row since all elements of curr row from 
            st_row+=1
            #now fill all elements from st_row up until the last row
            for i in range(st_row, end_row + 1):
                res.append(matrix[i][end_col])
            #move 1 col inside i.e. to the left
            end_col -=1
            if st_row > end_row or end_col < st_col:
                break
            #fill all elements on the last row for all columns up until 0
            for i in range(end_col, st_col - 1, -1):
                res.append(matrix[end_row][i])
            
            #Now, go up one row from the bottom, and fill all elements from that col to end col
            end_row-=1
            for i in range(end_row, st_row - 1, -1):
                res.append(matrix[i][st_col])
            #move one col inside
            st_col+=1
        return res