class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> hs = new HashSet<>();
        int ans=0;
        for(int ii:nums) {hs.add(ii);}
        for(int ii:hs) {
            if (!hs.contains(ii - 1)) {
                int m = ii + 1;
                while(hs.contains(m)) {
                    m++;
                }
                ans = Math.max(ans, m - ii);
            }
        }
        return ans;
    }
}
