# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global_ans = -float("inf")
        def get_max_sum(node):
            nonlocal global_ans
            if not node:
                return 0
            left_max = get_max_sum(node.left)
            left_max = max(0, left_max)
            right_max = get_max_sum(node.right)
            right_max = max(0, right_max)
            curr_max_sum = left_max + right_max + node.val
            global_ans = max(global_ans, curr_max_sum)
            return max(node.val, node.val + left_max, node.val + right_max)
        
        get_max_sum(root)
        
        return global_ans
        