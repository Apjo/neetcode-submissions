class Solution {
    public String minWindow(String s, String t) {
        if (s.equals(t)) {
            return t;
        }
        int prev=0, le=0, ri=0, L1 = s.length(), L2=t.length(), ans = Integer.MAX_VALUE;
        int required = L2;
        if (L1 < L2) {
            return "";
        }
        //maintain a freq map of characters in t, since we need to have t in s
        Map<Character, Integer> m1 = new HashMap<>();
        for(char cc : t.toCharArray()) {
            m1.put(cc, m1.getOrDefault(cc, 0) + 1);
        }
        while(ri < L1) {
            //continue going over to end of string S, while keeping a track of frequencies of matching chars in s and t
            //as soon as the freq. of a char drops to 0, update required param to decrement by 1
            char curr = s.charAt(ri);
            if (m1.containsKey(curr)) {
                m1.put(curr, m1.get(curr) - 1);
                if (m1.get(curr) >= 0) {
                    required--;
                }
            }
            ri++;
            while(le <= ri && required == 0) {
                char fromLe = s.charAt(le);
                //now that you have "covered" all the required chars in string t
                //determine whats the best len of the substring that contains all the chars in t
                int len = ri - le;
                if (len < ans) {
                    ans=len;
                    prev=le;
                }
                //now that you have got the best len, try to drop chars from left, and see whether or not there are chars that still make up string t
                if (m1.containsKey(fromLe)) {
                    m1.put(fromLe, m1.get(fromLe) + 1);
                    if (m1.get(fromLe) > 0) {
                        required++;
                    }
                }
                le++;
            }
        }
        return ans == Integer.MAX_VALUE ? "" : s.substring(prev, prev + ans);
    }
}
