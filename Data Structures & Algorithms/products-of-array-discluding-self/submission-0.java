class Solution {
    public int[] productExceptSelf(int[] nums) {
        int N = nums.length;
        int[]prodLeft = new int[N];
        int[]prodRight = new int[N];
        Arrays.fill(prodLeft, 1);
        Arrays.fill(prodRight, 1);
        int mult=1;
        for(int i=0; i < N; i++) {
            prodLeft[i] = mult;
            mult*=nums[i];
        }
        mult=1;
        for(int i = N - 1; i >= 0; i--) {
            prodRight[i] *= mult;
            mult*=nums[i];
        }
        for(int i=0; i< N; i++) {
            nums[i] = prodLeft[i] * prodRight[i];
        }
        return nums;
    }
}  
