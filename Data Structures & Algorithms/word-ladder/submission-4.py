class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        if the end word not in word list immediately return a 0
        try to use a BFS
        add to q the starting word
        while q is not empty:
            -poll
            -compare if this is equal to end word, if it is return ans
            -iterate over the wordlist:
                -if wordlist[i]==curr:
                    continue
                -compare freq_map[wordlist[i]] with freq_map[curr]:
                -if equal and not visited:
                    -add to q
                    -incremenet ans by 1
                    -mark wordlist[i] as visited
        return ans
        '''
        
        if endWord not in wordList:
            return 0
        if endWord == beginWord:
            return 0
        q = deque()
        q.append(beginWord)
        # q.append((beginWord, 1))
        ans = 1
        # def build_map(w):
        #     mm = {}
        #     for cc in w:
        #         mm[cc] = mm.get(cc, 0)+1
        #     return mm
        
        # def are_dicts_equal(d1, d2):
        #     if len(d1) != len(d2):
        #         return False
        #     if sorted(d1.values()) != sorted(d2.values()):
        #         return False
        #     shared_keys_count = sum(1 for k in d1 if k in d2)
        #     return shared_keys_count == len(d1) - 1

        visited = set()
        visited.add(beginWord)
        wordsSet = set(wordList)
        while q:
            N = len(q)
            for l in range(N):
                # curr, level = q.popleft()
                curr = q.popleft()
                # print(f"current={curr}, level={level}")
                if curr == endWord:
                    # ans+=1
                    # return level
                    return ans
                for w in range(len(curr)):
                    for cc in range(ord('a'), ord('z') + 1):
                    # Rebuild the string: [everything before] + [new letter] + [everything after]
                        curr2 = curr[:w] + chr(cc) + curr[w+1:]
                        if curr2 in wordsSet and curr2 not in visited:
                            # q.append((curr2, level+1))
                            q.append(curr2)
                            visited.add(curr2)
            ans+=1
        # return ans
        return 0
