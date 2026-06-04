class Solution {
    private static void rev(int[] arr, int i, int j) {
        while(i < j) {
            int tt = arr[i];
            arr[i] = arr[j];
            arr[j] = tt;
            i++;
            j--;
        }
    }
    public void rotate(int[] nums, int k) {
        int L = nums.length;
        k%=L;
        rev(nums, 0, L - 1);
        rev(nums, 0, k - 1);
        rev(nums, k, L - 1);

        // for(int i=0; i < L; i++) {
        //     int n = ((i+k) % L);
        //     int tt = nums[i];
        //     nums[i] = nums[n];
        //     nums[n] = tt;
        // }
    }
}