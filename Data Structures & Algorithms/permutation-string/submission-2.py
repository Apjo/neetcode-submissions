class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        #prepare a frequency map for s1
        freq={}
        for i in range(len(s1)):
            if s1[i] in freq:
                freq[s1[i]]+=1
            else:
                freq[s1[i]]=1
        print(f"freq map for s1={freq}")
        #iterate over s2:
        k = len(s1)
        M = len(s2)
        i=0
        ans=False
        while i < M:
            hm = {}
            j = i + k
            ss = s2[i : j]
            print(f"At i={i}, j={j} looking at substr={ss}")
            for ii in range(len(ss)):
                if ss[ii] in hm:
                    hm[ss[ii]]+=1
                else:
                    hm[ss[ii]]=1
            print(f"GOT HM={hm}")
            if hm != freq:
                ans=False
                # return False
            else:
                print("frequencies match!!!!")
                ans=True
                break
            i+=1
        return ans



            #in doing so, ignore characters that aren't present in s1 but are present in s2
            #if a char in s2 is present in s1, decrement its frequency by 1, if its 0 remove it 
            #continue until you see all frequencies for all characters to be 0, when
        #at the end check to see either all frequencies for all characters are 0 or not