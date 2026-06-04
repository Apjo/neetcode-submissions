class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int L = nums.length;
        int A = L - k + 1;
        //the final result set will contain nums.len - k + 1 elements
        int[] res = new int[A];
        Deque<Integer> dq = new ArrayDeque<>();
        //to set the current max for first window
        //for i in 0 to k
            //keep on adding to a queue as long as nums[i] is greater than the last element added
            //else remove from the queue if nums[i] >= queue's last element
        //now set the currmax for 0th index in the output array as the element at queue's top
        for(int i=0; i < k; i++) {
            while(!dq.isEmpty() && nums[i] >= nums[dq.peekLast()]) {
                dq.pollLast();    
            }
            dq.offerLast(i);
        }
        int idx=0;
        res[idx]=nums[dq.peekFirst()];
        idx++;
        //similarly, now from i in k to nums.len:
            //remove the index of the largest element in the queueif its location is outside the current sliding window i - k
            //keep on removing all indexes from the back fo the q where the element at those indexes are < nums[i]
            //add the ith or the "right" element to the back of the queue
            //set the element in res at location i-k+1 to be the largest element at front of the q
        for(int i=k; i < L; i++) {
            if (!dq.isEmpty() && i-k == dq.peekFirst()) {
                dq.pollFirst();
            }
            while(!dq.isEmpty() && nums[i] > nums[dq.peekLast()]) {
                dq.pollLast();
            }
            dq.offerLast(i);
            res[idx++]=nums[dq.peekFirst()];
        }
        return res;
    }
}
