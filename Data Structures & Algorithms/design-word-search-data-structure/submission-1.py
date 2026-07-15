class WordDictionary:
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.end_of_word = False
        def __repr__(self):
            return f"{self.children}"

    def __init__(self):
        self.root = self.TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            curr_child = curr.children.get(ch, None)
            if curr_child is None:
                curr.children[ch] = self.TrieNode()
            curr = curr.children[ch]
        curr.end_of_word = True
        
    #With wildcard — use DFS. At every ., iterate all 26 children and recurse into each non-null one. Return true the moment any branch succeeds.
    def search(self, word: str) -> bool:
        def solve(idx, curr):
            if idx >= len(word):
                return curr.end_of_word
        
            if word[idx] == ".":
                flag = False
                for ch in curr.children:
                    flag = flag or solve(idx+1, curr.children[ch])
                return flag
            elif curr.children.get(word[idx], None) is None:
                return False
            else:
                return solve(idx+1, curr.children[word[idx]])
        return solve(0, self.root)