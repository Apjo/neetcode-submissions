class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        If nums[i] is a negative number (e.g., -2), you want to multiply it by the smallest (most negative) possible previous product (e.g., -10) to get the biggest positive result (20).
        If nums[i] is a positive number (e.g., 3), you want to multiply it by the largest previous product (e.g., 10) to get 30.
        A highly negative number (like -10) is technically a "minimum" value. But the moment it hits another negative number, it instantly flips into a massive maximum value.If you don't track the current min, your code becomes "blind" to these negative flips, and it will miss the jackpot combination.
        '''
        curr_max, curr_min, res = 1,1,nums[0]
        for elem in nums:
            temp = elem * curr_max
            curr_max = max(elem, curr_max*elem, curr_min * elem)
            curr_min = min(elem, temp, curr_min * elem)
            res = max(res, curr_max)
        return res