class Solution {
    private static void swap(int[]arr, int a, int b) {
        int te = arr[a];
        arr[a] = arr[b];
        arr[b] = te;
    }
    public void sortColors(int[] nums) {
        int i=0, lo=0, hi = nums.length - 1;
        while(i <= hi) {
            switch(nums[i]) {
                case 0: swap(nums, lo, i);i++;lo++;break;
                case 2: swap(nums, hi, i); hi--;break;
                case 1 : i++;break;
            }
        }
    }
}