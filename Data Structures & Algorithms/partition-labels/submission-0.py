class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mp = {}
        N = len(s)
        for i in range(N):
            #add to mp the lastInfexOf each char
            mp[s[i]] = s.rindex(s[i])
        print(mp)
        res, st, end, i = [], 0, 0, 0
        while i < N:
            end = max(end, mp[s[i]])
            if i == end:
                part_len = end - st + 1
                res.append(part_len)
                st=i+1
                # print(f"found match at i={i}, end={end}, st={st}, len={part_len}")
            i+=1
        return res