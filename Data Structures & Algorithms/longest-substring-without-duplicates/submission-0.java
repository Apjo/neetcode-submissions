class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> freq = new HashMap<>();
        int le=0,ans=0;
        for(int right=0; right < s.length(); right++) {
            char curr = s.charAt(right);
            freq.put(curr, freq.getOrDefault(curr, 0) + 1);
            //if (freq.get(curr) > 1) {
                while(le < right && freq.get(curr) > 1) {
                    //drop left most
                    char toRem = s.charAt(le);
                    freq.put(toRem, freq.get(toRem) -1);
                    if (freq.get(toRem) == 0) {
                        freq.remove(toRem);
                    }
                    le++;
                    //remove from map when freq reaches 0
                }
                ans=Math.max(ans, right - le + 1);
            //}
        }
        return ans;
    }
}
