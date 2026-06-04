class Solution {
    public int characterReplacement(String s, int k) {
        /*
        iterate over the string, for each character do:
        - keep a track of the frequency of occurrence
        - keep track of max frequency of a char
        - move the right pointer to the right, one by one, until (length of the substring) - (the "count of most popular character") = k
        while le <= ri AND the remaining_num_characters_to_replace is > k:
            - drop the char from left
            - increment left pointer
        -keep track of max len
        -return the max len
        */
        int left=0, ans=0, maxFreqSoFar=0;
        Map<Character, Integer> freq = new HashMap<>();
        for(int right = 0; right < s.length(); right++) {
            char curr = s.charAt(right);
            freq.put(curr, freq.getOrDefault(curr, 0) + 1);
            maxFreqSoFar = Math.max(maxFreqSoFar, freq.get(curr));
            int remChars = (right-left + 1) - maxFreqSoFar;
            if (left <= right && remChars > k) {
                freq.put(s.charAt(left), freq.get(s.charAt(left)) - 1);
                left++;
            }
            ans = Math.max(ans, (right - left + 1));
        }
        return ans;
    }
}
