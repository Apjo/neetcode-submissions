class Solution {
    public int[] getConcatenation(int[] nums) {
        int[]ans2 = new int[nums.length * 2];
        int L = nums.length;
        for(int i=0; i < ans2.length; i++) {
            ans2[i] = nums[i % L];
        }
        return ans2;

    }
}