class Solution {
    public int subarraySum(int[] nums, int k) {
        Map<Integer, Integer> freq = new HashMap<>();
        int ans=0, currSum=0;
        freq.put(0, 1);
        for(int i=0; i < nums.length; i++) {
            currSum +=nums[i];
            int diff = currSum - k ;
            ans+=freq.getOrDefault(diff, 0);
            freq.put(currSum, freq.getOrDefault(currSum, 0) + 1);
        }
        return ans;
    }
}