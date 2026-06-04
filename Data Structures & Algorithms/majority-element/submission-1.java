class Solution {
    public int majorityElement(int[] nums) {
        int candidate = nums[0], ctr=1;
        for(int ii : nums) {
            if(ctr == 0) {
                candidate = ii;
                ctr=1;
            } else if(ii == candidate) {
                ctr++;
            } else {
                ctr-=1;
            }
        }
        return candidate;

    }
}