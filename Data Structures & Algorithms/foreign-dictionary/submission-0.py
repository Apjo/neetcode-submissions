class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #build graph
        n = 26
        G=[[False for _ in range(n)] for _ in range(n)]
        st=[]
        captured=[-1]*(n)
        #get the first word
        first_word = words[0]
        #set all its characters as unvisited
        for cc in first_word:
            captured[ord(cc) - ord('a')]=0
        
        for i in range(1, len(words)):
            next_word = words[i]
            #if the next_word is the prefix of first_word, this case isnt possible
            if words[0] != next_word and words[0].startswith(next_word):
                captured=[2]*(n)
                break
            
            for ch in next_word:
                 captured[ord(ch) - ord('a')]=0
            
            min_len = min(len(first_word), len(next_word))
            for i in range(min_len):
                if first_word[i] != next_word[i]:
                    G[ord(first_word[i]) - ord('a')][ord(next_word[i]) - ord('a')] = True
                    break
            first_word = next_word
        
        def solve(vertex):
            captured[vertex]=1
            for neighbor in range(26):
                if G[vertex][neighbor]:
                    if captured[neighbor]==1:
                        return True
                    if captured[neighbor]==0:
                        ans = solve(neighbor)
                        if ans:
                            return True
            captured[vertex]=2
            st.append(chr(vertex + ord('a')))
            return False
        
        #return output str
        res=""
        for v in range(n):
            if captured[v] == 0:
                #if there exists a cycle, return empty str as is
                if solve(v):
                    return ""
        
        #apply some form of toposort
        
        while st:
            res+=st.pop()
        return res