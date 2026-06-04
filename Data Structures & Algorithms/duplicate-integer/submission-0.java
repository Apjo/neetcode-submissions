class Solution {
    public boolean hasDuplicate(int[] nums) {
        int L = nums.length;
        Set<Integer> hs = new HashSet<>();
        for(int i:nums) {
            hs.add(i);
        }
        return hs.size() == L ? false:true;
    }
}