class Solution {
    public int removeElement(int[] nums, int val) {
        int pos = 0;
        for(int i=0; i < nums.length; ) {
            if(nums[i] != val) {
                nums[pos] = nums[i];
                pos++;
            }
            i++;
        }
        return pos;
    }
}