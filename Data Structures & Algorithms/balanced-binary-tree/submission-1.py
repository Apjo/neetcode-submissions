# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def ht(n):
            if not n:
                return 0
            return 1 + max(ht(n.left), ht(n.right))
        if not root:
            return True
        lht = ht(root.left)
        print(f"L ht={lht}")
        rht = ht(root.right)
        print(f"R ht={rht}")
        diff = lht - rht
        print(f"ht diffs={diff}")
        if abs(diff) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)