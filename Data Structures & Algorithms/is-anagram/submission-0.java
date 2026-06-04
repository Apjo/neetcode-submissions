class Solution {
    public boolean isAnagram(String s, String t) {
        if (t.length() != s.length()) { return false; }
        if (t.equals(s)) { return true; }
        int[]freq = new int[26];
        for(int i=0; i < s.length(); i++) {
            char c = s.charAt(i);
            int d = c - 'a';
            freq[d]++;
        }
        for(int i=0; i < t.length(); i++) {
            char c = t.charAt(i);
            int d = c - 'a';
            freq[d]--;
        }
        for(int i : freq) {
            if(i != 0) {
                return false;
            }
        }
        return true;
    }
}
