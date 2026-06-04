class Solution {
    public int numRescueBoats(int[] people, int limit) {
        Arrays.sort(people);
        int lo=0, hi = people.length - 1, ctr=0;
        while(lo <= hi) {
            int ss = people[lo] + people[hi];
            if (ss <= limit) {
                ctr++;
                lo++;
                hi--;
            } else {
                ctr++;
                hi--;
            }
        }
        return ctr;
    }
}