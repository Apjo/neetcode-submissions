class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int L = nums.length;
        int[]res = new int[L -k + 1];
        PriorityQueue<Integer> maxH = new PriorityQueue<>((a, b) -> Integer.compare(nums[b], nums[a]));
        for(int right=0; right < L; right++) {
            int windowLen = right - k + 1;
            while(!maxH.isEmpty() && windowLen > maxH.peek()) {
                maxH.poll();
            }
            maxH.offer(right);
            if (windowLen >= 0) {
                res[right - k + 1] = nums[maxH.peek()];
            }
        }
        return res;
    }
}
