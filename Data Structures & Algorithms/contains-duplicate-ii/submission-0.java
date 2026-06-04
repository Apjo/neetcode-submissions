class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Map<Integer, Integer> idx = new HashMap<>();
        for(int r=0; r < nums.length; r++) {
            if(idx.containsKey(nums[r]) && r - idx.get(nums[r]) <= k) {
                return true;
            }
            idx.put(nums[r], r);
        }
        return false;
    }
}