class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        all_sum = sum(nums)
        if all_sum % 2 != 0:
            return False
        all_half = int(all_sum / 2)

        def solve(idx, prev_sum) -> bool:
            if (idx, prev_sum) in memo:
                return memo[(idx, prev_sum)]
            
            if prev_sum == all_half:
                return True

            if idx >= N or prev_sum > all_half:
                return False

            new_sum = prev_sum + nums[idx]

            ans = solve(idx + 1, new_sum)
            if ans:
                memo[(idx, prev_sum)] = ans
                return True
            
            ans = solve(idx + 1, prev_sum)
            if ans:
                memo[(idx, prev_sum)] = ans
                return True

            # we got till here, we tried PICK it failed, we tried SKIP it too failed, so ultimately we return a False
            memo[(idx, prev_sum)] = False
            return False
        memo={}
        return solve(0, 0)
        