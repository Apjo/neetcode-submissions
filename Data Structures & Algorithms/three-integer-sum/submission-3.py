class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)):
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                ss = nums[i] + nums[lo] + nums[hi]
                if ss == 0:
                    # temp = [[nums[i], nums[lo], nums[hi]]]
                    # print(temp)
                    res.append([nums[i], nums[lo], nums[hi]])
                    lo+=1
                    hi-=1
                    # res.add(temp)
                    # break
                elif ss < 0:
                    lo +=1
                else:
                    hi-=1
        # print(res)
        unique_tuples = set(tuple(item) for item in res) 
        # res2 = set(tuple(inner_list) for inner_list in res)
        return list(unique_tuples)