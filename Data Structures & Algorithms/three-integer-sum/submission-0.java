class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Set<List<Integer>> res = new HashSet<>();
        Arrays.sort(nums);
        //Set<Integer> j = new HashSet<>();
        for(int i=0; i < nums.length; i++) {
            int le = i + 1, ri = nums.length - 1;
            while(le < ri) {
                int ss = nums[i] + nums[le] + nums[ri];
                if (ss == 0) {
                    res.add(Arrays.asList(nums[i], nums[le], nums[ri]));
                    le+=1;ri-=1;
                } else if(ss < 0) {
                    le+=1;
                } else {
                    ri-=1;
                }
            }
            //List<Integer> temp = new ArrayList<>(j);
            //res.add(temp);
        }
        return new ArrayList<>(res);
    }
}
