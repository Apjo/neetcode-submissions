class Solution {
    private static String hashIt(String s) {
        int[]ctr = new int[26];
        for(char cc : s.toCharArray()) {
            ctr[cc - 'a']++;
        }
        String gg =  Arrays.toString(ctr);
        return gg;
    }
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> freq = new HashMap<>();
        for(String s : strs) {
            String hh = hashIt(s);
            if (!freq.containsKey(hh)) {
                freq.put(hh, new ArrayList<>());
            }
            freq.get(hh).add(s);
            
        }
        return new ArrayList<>(freq.values());
    }
}
