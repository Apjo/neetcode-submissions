class Solution {
    public boolean isPalindrome(String s) {
        int le=0, ri = s.length() - 1;
        while(le < ri) {
            while (le < ri && !Character.isLetterOrDigit(s.charAt(le))) {
                le++;
            }
            while (ri > le && !Character.isLetterOrDigit(s.charAt(ri))) {
                ri--;
            }
            if (Character.toLowerCase(s.charAt(le)) != Character.toLowerCase(s.charAt(ri))) {
                return false;
            }
            le++;ri--;
        }
        return true;
    }
}
