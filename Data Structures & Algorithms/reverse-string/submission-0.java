class Solution {
    public void reverseString(char[] s) {
        int le=0, ri = s.length - 1;
        while(le < ri) {
            char tt = s[le];
            s[le] = s[ri];
            s[ri] = tt;
            le++;
            ri--;
        }
    }
}