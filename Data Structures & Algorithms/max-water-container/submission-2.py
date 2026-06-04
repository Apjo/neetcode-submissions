class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right, ans=0, len(heights) - 1, float("-inf")
        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            area = width * height
            ans=max(ans, area)
            if heights[left] <= heights[right]:
                left+=1
            else:
                right-=1
        return ans