# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #what if both nodes dont exists
      #only one node exists
      #both node exists
      #both nodes are same
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return root
        if root.val == p.val or root.val == q.val:
            return root
        lca_le = self.lowestCommonAncestor(root.left, p, q)
        lca_ri = self.lowestCommonAncestor(root.right, p, q)
        if not lca_le and not lca_ri:
            return None
        if lca_le and lca_ri:
            return root
        if not lca_le and lca_ri:
            return lca_ri
        else:
            return lca_le