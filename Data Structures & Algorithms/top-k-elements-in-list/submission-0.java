class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> m = new HashMap<>();
        for(int ii: nums) {
            m.put(ii, m.getOrDefault(ii, 0) + 1);
        }
        PriorityQueue<Map.Entry<Integer, Integer>> minH = new PriorityQueue<>(
            (a, b) -> Integer.compare(a.getValue(), b.getValue()));
        for(Map.Entry<Integer, Integer> e: m.entrySet()) {
            minH.offer(e);
            if(minH.size() > k) {
                minH.poll();
            }
        }
        int[]op = new int[k];
        int c = 0;
        while(!minH.isEmpty()) {
            op[c++] = minH.poll().getKey();
        }
        return op;
    }
}
