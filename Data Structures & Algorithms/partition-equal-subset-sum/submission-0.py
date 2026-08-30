class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        ans,H, N = False, int(len(nums) / 2), len(nums)
        all_sum = sum(nums)
        if all_sum % 2 !=0:
            return False
        found_half_sum = False
        all_half = int(all_sum / 2)
        def solve(idx, prev):
            nonlocal found_half_sum
            print(f"Entering at index={idx}, prev sum={prev}")
            # nonlocal ans
            if idx >= N:
                print("OUTOF BOUNDS! returning")
                if prev == all_half:
                    found_half_sum=True
                else:
                    found_half_sum=False
                return
            if found_half_sum:
                return
            if prev > all_half:
                print(f"curr sum={prev} > 1/2 sum={all_half}")
                found_half_sum=False
                return
            if prev == all_half:
                print(f"MATCH curr sum={prev} == 1/2 sum={all_half}")
                found_half_sum=True
                return
            prev+=nums[idx]
            print(f"PICK num={nums[idx]} at idx={idx}, new sum={prev}")
            solve(idx+1, prev)
            prev-=nums[idx]
            print(f"SKIP to next index={idx+1}, curr sum={prev}")
            solve(idx+1, prev)
        
        solve(0,0)
        return found_half_sum