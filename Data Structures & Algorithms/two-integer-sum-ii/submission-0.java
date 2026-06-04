class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int lo=0, hi = numbers.length - 1;
        int[]res = new int[2];
        while(lo < hi) {
            int ssum = numbers[lo] + numbers[hi];
            if (ssum == target) {
                res[0] = lo + 1;
                res[1] = hi + 1;
                return res;
            } else if (ssum < target) {
                lo++;
            } else {
                hi--;
            }
        }
        return res;
    }
}
