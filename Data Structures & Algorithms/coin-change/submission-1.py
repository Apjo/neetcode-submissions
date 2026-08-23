class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ans = float("inf")
        memo={}
        def solve(T, idx):
            # nonlocal ans
            # print(f"Starting with T={T}, index={idx}, current memo={memo}")
            if idx >= len(coins):
                # print(f"REACHED END OF ARR with T={T}, index={idx}, current memo={memo}")
                if T != 0:
                    memo[(T, idx)] = float("inf")
                    return memo[(T, idx)]
                if T == 0:
                    memo[(T, idx)] = 0
                    return memo[(T, idx)]
            
            if T < 0:
                # print(f"INVALID T={T}, index={idx}, current memo={memo}")
                memo[(T, idx)] = float("inf")
                # return -1
                return memo[(T, idx)]

            if T == 0:
                #we have an answer! but where do we get the min from?
                # print(f"GOT IT! T={T}, index={idx}, current memo={memo}")
                memo[(T, idx)] = 0
                return memo[(T, idx)]
            
            if (T, idx) in memo:
                # print(f"{T}, {idx} in MEMO!")
                return memo[(T, idx)]
            else:
                memo[(T, idx)] = float("inf")
            # if you pick this coin, since there are infinite denominations, we can just stay here, and continue down this path where we keep on picking this coin at idx itself, and decrementing T by coins[idx] value, till we either reach a 0 where we found the min number of coins required, or we reach a -1 where we would never be able to reach the target.
            a = solve(T - coins[idx], idx) + 1
            # print(a)
            b = solve(T, idx + 1)
            # print(b)
            if a and b:

                memo[(T, idx)] = min(a, b)
                # print(f"SETTING MIN! T={T}, index={idx} answer from pick={a}, from not pick={b}, final ans={min(a, b)}")
            return memo[(T, idx)]
        val = solve(amount, 0)
        return val if val != float("inf") else -1
        # return solve(amount, 0) 
        