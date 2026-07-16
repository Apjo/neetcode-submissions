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
                # flag = False
                for child_node in curr.children.values():
                    if solve(idx + 1, child_node):
                        return True
                return False
            else:
                if word[idx] not in curr.children:
                    return False
                return solve(idx + 1, curr.children[word[idx]])
        return solve(0, self.root)