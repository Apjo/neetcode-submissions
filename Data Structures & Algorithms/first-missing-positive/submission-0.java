class Solution {
    public int firstMissingPositive(int[] nums) {
        int L = nums.length;
        int i=0;
        while(i < L) {
            while(nums[i] != i+1) {
                int destIndex = nums[i] - 1;
                if (destIndex >= 0 && destIndex < L && nums[i] != nums[destIndex]) {
                    int tt = nums[i];
                    nums[i] = nums[destIndex];
                    nums[destIndex] = tt;
                } else {
                    break;
                }
            }
            i++;
        }
        for(int idx=0; idx < L; idx++) {
            if(nums[idx] != idx + 1) {
                return idx + 1;
            }
        }
        return L + 1;
    }
}