class Solution {
    public boolean isPalindrome(String s) {
        //preprocess? -> lower case, remove non-alphanumer chars
        s=s.toLowerCase();
        StringBuilder sb = new StringBuilder();
        for(char cc : s.toCharArray()) {
            
            if(Character.isLetter(cc) || Character.isDigit(cc)) {
                sb.append(cc);
            }
        }
        //2 pointers
        int le=0, ri=sb.length() - 1;
        while(le < ri) {
            if(sb.charAt(le) != sb.charAt(ri)) {
                return false;
            }
            le++;
            ri--;
        }
        return true;
    }
}
