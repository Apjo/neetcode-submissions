# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #we calculate diameter at the same time we are calculating ht of the tree
        global_dia = 0
        
        #for each node during dfs
        def dfs(n):
            nonlocal global_dia
            if not n:
                return 0
            #get left ht
            left_ht = dfs(n.left)
            #get right ht
            right_ht = dfs(n.right)
            #calc. dia through this node = left ht + right ht
            curr_dia = left_ht + right_ht
            #update the global answer = max(curr_dia, global_dia)
            global_dia = max(global_dia, curr_dia)
            
            #return the ht to the parent node
            return 1 + max(left_ht, right_ht)
        
        dfs(root)
        return global_dia