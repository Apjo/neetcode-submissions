class Solution {
    public int trap(int[] height) {
        int ans=0, leftMax=height[0], rightMax=height[height.length - 1],le=0,ri=height.length - 1;
        while(le < ri) {
            if (leftMax < rightMax) {
                le++;
                if(height[le] > leftMax) {
                    leftMax = height[le];
                } else {
                    ans+=leftMax - height[le];
                }
            } else {
                ri--;
                if(height[ri] > rightMax) {
                    rightMax = height[ri];
                } else {
                    ans+=rightMax - height[ri];
                }
            }
        }
        return ans;
    }
}
