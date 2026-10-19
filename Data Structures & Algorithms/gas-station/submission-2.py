class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        ans, x = 0, 0
        N = len(gas)
        for i in range(N):
            x+=(gas[i] - cost[i])
            # ans=i
            if x < 0:
                x=0
                ans = i + 1
        return ans
        