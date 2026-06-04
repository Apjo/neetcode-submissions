class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk=[]
        ans,N = 0,len(heights)
        for i in range(N + 1):
            while stk and (i == N or heights[stk[-1]] >= heights[i]):
                idx = stk.pop()
                ht=heights[idx]
                w = i if not stk else i - stk[-1] - 1
                ans = max(ans, ht * w)
            stk.append(i)
        return ans