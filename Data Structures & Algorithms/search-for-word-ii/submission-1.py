class Solution:
    class TrieNode:
        def __init__(self):
            self.children={}
            self.eow=False
            self.word=""
    
    class MyTrie:
        def __init__(self, words:List[str]):
            self.root = Solution.TrieNode()
            for word in words:
                self.insert(word)

        def insert(self, word: str):
            curr = self.root
            for ch in word:
                # curr_child = curr.children.get(ch, None)
                if ch not in curr.children:
                    curr.children[ch] = Solution.TrieNode()
                curr=curr.children[ch]
            curr.eow=True
            curr.word = word

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #store each word in a trie
        word_trie = self.MyTrie(words)
        M, N = len(board), len(board[0])
        visited = [[False for _ in range(N)] for _ in range(M)]
        res=set()

        def dfs_solve(row, col, curr_node, visited):
            # if row < 0 or row >= M or col < 0 or col >= N or visited[row][col]:
            #     return
            
            if row < 0 or row >= M or col < 0 or col >= N or board[row][col]=="#":
                return
            
            if board[row][col] in curr_node.children:
                curr = curr_node.children[board[row][col]]
                if curr.eow:
                    res.add(curr.word)

                # visited[row][col] = True
                temp = board[row][col]
                board[row][col]="#"
                dfs_solve(row+1, col, curr, visited)
                dfs_solve(row-1, col, curr, visited)
                dfs_solve(row, col+1, curr, visited)
                dfs_solve(row, col-1, curr, visited)
                # visited[row][col] = False
                board[row][col]=temp

        for r in range(M):
            for c in range(N):
                dfs_solve(r, c, word_trie.root, visited)
        
        return list(res)
    