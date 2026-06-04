class Solution {
    public int[] productExceptSelf(int[] nums) {
        int N = nums.length;
        int mult=1;
        int[]temp = new int[N];
        temp[0]=1;
        for(int i=1; i < N; i++) {
            temp[i] = temp[i - 1] * nums[i - 1];
        }
        for(int i = N - 1; i >= 0; i--) {
            temp[i]*=mult;
            mult*=nums[i];
        }
        return temp;
    }
}  
