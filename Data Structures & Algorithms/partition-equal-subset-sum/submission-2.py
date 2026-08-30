class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        all_sum = sum(nums)
        if all_sum % 2 !=0:
            return False
        all_half = int(all_sum / 2)

        def solve(idx, prev) -> bool:
            print(f"Entering at index={idx}, prev sum={prev}")
            if idx >= N:
                print("OUTOF BOUNDS! returning")
                if prev == all_half:
                    return True
                return False

            if prev > all_half:
                return False
            
            if prev == all_half:
                return True
            
            prev+=nums[idx]
            print(f"PICK num={nums[idx]} at idx={idx}, new sum={prev}")
            ans = solve(idx+1, prev)
            if ans:
                return True
            prev-=nums[idx]
            print(f"SKIP to next index={idx+1}, curr sum={prev}")
            ans = solve(idx+1, prev)
            if ans:
                return True
            #we got till here, we tried PICK it failed, we tried SKIP it too failed, so ultimately we return a False
            return False
            
        
        return solve(0,0)
        