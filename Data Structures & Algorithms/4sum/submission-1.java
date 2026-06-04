class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
       Set<List<Integer>> res = new HashSet<>();
       int L = nums.length;
       Arrays.sort(nums);
       for(int i=0; i < L; i++) {
        for(int j=i+1; j < L; j++) {
            int le=j+1, ri = L - 1;
            while(le < ri) {
                long ss = ((long)nums[i]+(long)nums[j]+(long)nums[le]+(long)nums[ri]);
                if (ss == target) {
                    res.add(Arrays.asList(nums[i],nums[j],nums[le],nums[ri]));
                    le++;
                    ri--;
                } else if(ss < target) {
                    le++;
                } else {
                    ri--;
                }
            }
        }
       }
       return new ArrayList<>(res); 
    }
}