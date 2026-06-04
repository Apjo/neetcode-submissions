class Solution {
    public int maxProfit(int[] prices) {
        int prev=prices[0], ans=0;
        for(int i=1; i < prices.length; i++) {
            if (prices[i] > prev) {
                ans+=prices[i] - prev;
                
            }
            prev=prices[i];
        }
        return ans;
    }
}