class Solution {
    public int maxArea(int[] heights) {
        int ans = Integer.MIN_VALUE;
        int lo=0, hi = heights.length - 1;
        for(int i=0; i < heights.length; i++) {
            while(lo < hi) {
                int breadth = hi - lo;
                int length = Math.min(heights[lo], heights[hi]);
                int area = breadth * length;
                ans=Math.max(ans, area);
                if(heights[lo] < heights[hi]) {
                    lo++;
                } else {
                    hi--;
                }
            }
        }
        return ans;
    }
}
