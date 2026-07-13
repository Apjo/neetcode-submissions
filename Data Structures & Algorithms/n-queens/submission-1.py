class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #use backtracking, place a queen on a location, run the validity check, if valid, proceed to place next queen,
        #else try placing the queen at a different location
        def is_valid(r, c) -> bool:
            
            temp_r = r-1
            temp_c = c-1

            #check if Q on diagonal left above me
            while temp_r >= 0 and temp_c >= 0:
                if board[temp_r][temp_c] == 'Q':
                    return False
                temp_r -= 1
                temp_c -= 1
            
            temp_r = r-1
            temp_c = c+1
            #check if a Q diagonal right above me
            while temp_r >=0 and temp_c < n :
                if board[temp_r][temp_c] == 'Q':
                    return False
                temp_r-=1
                temp_c +=1
            
            temp_r = r-1
            # #check if a Q in the same col as I am
            while temp_r >= 0:
                if board[temp_r][c] == 'Q':
                    return False
                temp_r-=1
        
            return True
        
        def solve(start_row, res, buff):
            if start_row == n:
                # for curr_row in range(n):
                    # print(f"curr row in board={board[curr_row]}")

                    # buff.append("".join(board[curr_row]))
                row_copy = ["".join(r) for r in board]
                # res.append(buff[:])
                res.append(row_copy)
                return

            for c in range(n):
                if is_valid(start_row, c):
                    board[start_row][c]='Q'
                    solve(start_row+1, res, buff)
                    board[start_row][c]='.'
        
        board = [["." for _ in range(n)] for _ in range(n)]
        if n == 1:
            return [["Q"]]
        if n > 1 and n <= 3 :
            return []
        
        res, buff = [], []
        
        solve(0, res, buff)
        
        return res