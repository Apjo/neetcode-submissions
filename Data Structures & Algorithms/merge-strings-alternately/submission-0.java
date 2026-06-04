class Solution {
    public String mergeAlternately(String word1, String word2) {
        int i=0, j = 0, L = word1.length(), M=word2.length();
        StringBuilder sb = new StringBuilder();
        while(i < L && j < M) {
            sb.append(word1.charAt(i++));
            sb.append(word2.charAt(j++));
        }
        while(i < L) {
            sb.append(word1.charAt(i++));
        }
        while(j < M) {
            sb.append(word2.charAt(j++));
        }
        return sb.toString();
    }
}