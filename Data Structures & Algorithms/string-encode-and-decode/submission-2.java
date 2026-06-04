class Solution {

    public static String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for(String s : strs) {
            int L = s.length();
            sb.append(L).append("#").append(s);
        }
        return sb.toString();
    }

    public static List<String> decode(String str) {
        List<String> res = new ArrayList<>();
        int i=0;
        while(i < str.length()) {
            int x=0;
            System.out.println("Starting at i=" + i);
            if (Character.isDigit(str.charAt(i))) {
                System.out.println("Found digit");
                while(i < str.length() && Character.isDigit(str.charAt(i))) {
                    x=x*10 + str.charAt(i) -'0';
                    i++;
                }
                System.out.println("Found len="+x);
            }
            if (str.charAt(i) == '#') {
                System.out.println("Found # at i="+i);
                i++;   
            }
            System.out.println("Skipping #");
            System.out.println("Now at="+i);
            String sn = str.substring(i, i + x);
            System.out.println("Found str="+sn);
            i=i+x;
            System.out.println("Next loc of i="+i);
            x=0;
            res.add(sn);
        }
        return res;
    }
}
