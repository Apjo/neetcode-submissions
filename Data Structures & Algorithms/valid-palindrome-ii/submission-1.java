class Solution {
    private static boolean isPalindrome(char[] arr, int lo, int hi) {
        while(lo < hi) {
            if(arr[lo] != arr[hi]) {
                return false;
            }
            lo++;hi--;
        }
        return true;
    }
    public boolean validPalindrome(String s) {
        int lo=0, hi = s.length() - 1;
        char[]arr = s.toCharArray();
        while(lo < hi) {
            if (arr[lo] != arr[hi]) {
            //drop one char from left end, and 1 char from right end
            //check for palindrome
                if (isPalindrome(arr, lo + 1, hi) || isPalindrome(arr, lo, hi - 1)) {
                    return true;
                } else {
                    return false;
                }
            }
            lo++;hi--;
        }
        return true;
    }
}