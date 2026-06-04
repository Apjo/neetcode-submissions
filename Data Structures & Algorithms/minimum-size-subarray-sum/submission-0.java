class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int currSum=0, left=0, ans=Integer.MAX_VALUE;
        for(int right=0; right < nums.length; right++) {
            currSum += nums[right];
            while(left <= right && currSum >= target) {
                currSum -= nums[left];
                ans = Math.min(ans, right - left + 1);
                left++;
            }
        }
        return ans==Integer.MAX_VALUE ? 0 : ans;
    }
}