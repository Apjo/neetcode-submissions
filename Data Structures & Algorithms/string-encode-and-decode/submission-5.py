import json

class Solution:
    # hm = {}
    def encode(self, strs: List[str]) -> str:
    # res=""
        hm={}
        for i in range(len(strs)):
            # print(f"looking at={strs[i]}, i={i}")
            inner_hm={}
            for cc in range(len(strs[i])):
                inner_hm[cc]=strs[i][cc]
            hm[i]=inner_hm
        return json.dumps(hm)

    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        hm1 = json.loads(s)
        # while i < len(s):
        #     curr_char = s[i]
        #     if 

        for k,inner_dict in hm1.items():
            inner_str=""
            for inner_k, inner_v in inner_dict.items():
                inner_str+=inner_v
            res.append(inner_str)
        return res