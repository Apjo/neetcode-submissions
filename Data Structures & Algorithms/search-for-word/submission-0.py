class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word or not board:
            return False
        
        def solve(idx, row, col, visited):
            if idx == len(word):
                return True
                
            if row < 0 or row >= M or col < 0 or col >= N or board[row][col] != word[idx] or visited[row][col]:
                return False

            idx+=1
            visited[row][col] = True
            found = (solve(idx, row + 1, col, visited) or
                    solve(idx, row - 1, col, visited) or
                    solve(idx, row, col + 1, visited) or
                    solve(idx, row, col - 1, visited))
            visited[row][col] = False
            return found
        
        M,N = len(board), len(board[0])
        visited = [[False for _ in range(N)] for _ in range(M)]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        idx=0
        for row in range(M):
            for col in range(N):
                # if board[row][col] == word[0]:
                    if solve(idx, row, col, visited):
                        return True
        return False

