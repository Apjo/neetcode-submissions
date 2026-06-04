# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def solve(n):
            if not n:
                return 0
            al,ar=0,0
            if n.left:
                al = solve(n.left)
            if n.right:
                ar = solve(n.right)
            return 1 + max(al, ar)

        return solve(root)