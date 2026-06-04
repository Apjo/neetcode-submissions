# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans=0
        n=0
        def solve(node):
            nonlocal ans,n
            if node.left:
                # ans+=1
                solve(node.left)
                # return solve(node.left)
            #do something with node
            ans+=1
            if ans == k:
                n=node.val
                return
            if node.right:
                # ans+=1
                solve(node.right)
        if not root:
            return -1
        
        solve(root)
        return n