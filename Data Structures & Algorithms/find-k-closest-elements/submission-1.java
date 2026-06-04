class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        List<Integer> res = new ArrayList<>();
        int lo=0, hi = arr.length - 1;
        //basically we are ruling out the furthest element each time either the leftmost, or the rightmost one.
        //When we get a window of size k, we found a solution, so if N is size of the input array, then we "rule out" N - k elements
        //int ruleOut = arr.length - k;
        while(hi - lo >= k) {
            if (Math.abs(arr[lo] - x) <= Math.abs(arr[hi] - x)) {
                hi--;
            } else {
                lo++;
            }
        }
        for(int i=lo; i <= hi; i++) {
            res.add(arr[i]);
        }
        return res;
    }
}