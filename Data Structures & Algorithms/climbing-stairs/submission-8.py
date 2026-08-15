class Solution:
    def climbStairs(self, n: int) -> int:
        if 0 <= n <= 2:
            return n

        memo=[-1]*(n+1)
        memo[0]=0
        memo[1]=1
        memo[2]=2 
        def solve(idx):
            # if idx == 0:
            #     return memo[0]
            # if idx == 1:
            #     return memo[1]
            # print(f"working with idx={idx}")
            if memo[idx]!= -1:
                # print(f"at idx={idx}, returning {memo[idx]}!")
                return memo[idx]
            # print(f"looking at indices={idx-1}, and {idx-2}")
            memo[idx] = solve(idx - 1) + solve(idx - 2)
            # print(f"updated idx={idx} to have a value of {memo[idx]}")
            return memo[idx]
        return solve(n)