# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def get_max_sum(n):
            if not n:
                return 0
            if not n.left and not n.right:
                return n.val
            le, ri = float("-inf"), float("-inf")
            if n.left:
                le = get_max_sum(n.left)
            if n.right:
                ri = get_max_sum(n.right)
            
            return max(n.val, n.val + le, n.val + ri)
        
        if not root:
            return float("-inf")
        if not root.left and not root.right:
            return root.val
        
        
        left_s = get_max_sum(root.left)
        right_s = get_max_sum(root.right)
        curr_s = root.val + max(0,left_s) + max(0, right_s)

        # if root.left and root.right:
        sub_sum = max(self.maxPathSum(root.left), self.maxPathSum(root.right))
        return max(curr_s, sub_sum)