class Solution:
    def rob(self, nums: List[int]):
        #time: N unique subproblems (indices 0 through len(nums)-1). Each one does O(1) work (lookup, arithmetic, memo assignment). So total time = N × O(1) = O(N).
        #Space is O(N): memo dict stores N entries + recursion stack depth up to N
        def solve(idx):
            if idx in memo:
                return memo[idx]
            #base cases
            if idx == 0:
                memo[0] = nums[0]
                return nums[0]
            if idx == 1:
                memo[1] = max(nums[0], nums[1])
                return max(nums[0], nums[1])

            #recursive case
            b = solve(idx - 2) + nums[idx]

            a = solve(idx - 1)

            memo[idx] = max(a, b)
            
            return max(a, b)

        memo = {}
        return solve(len(nums) - 1)
        