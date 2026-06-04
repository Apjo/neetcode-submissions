# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        print("hiiii")
        def dfs(n, m) -> bool:
            if n is None and m is None:
                return True
            if n is None and m is not None or n is not None and m is None:
                return False
            print(f"at roots={n.val} and {m.val}")
            #children are same
            # if n.left is None and n.right is None and m.left is None and m.right is None and n.val == m.val:
            #     return True
            if n.val != m.val:
                return False
            print(f"root vals are same check children")
            
            is_left, is_right=False, False
            
            #if both children on left are present
            if n.left is not None and m.left is not None:
                print(f"going left of n and m roots")
                is_left = dfs(n.left, m.left)
                print(f"from left got answer={is_left}")
            
            #either m's left child is present or n's
            if n.left is not None and m.left is None or n.left is None and m.left is not None:
                is_left=False
            if n.val == m.val and n.left is None and m.left is None:
                is_left=True

            #both right children are present
            if n.right is not None and m.right is not None:
                print(f"going right of n and m roots")
                is_right = dfs(n.right, m.right)
                print(f"from right got answer={is_right}")
            #either m's right child is present or n's
            if n.right is not None and m.right is None or n.right is None and m.right is not None:
                is_right=False
            if n.val == m.val and n.right is None and m.right is None:
                is_right=True
            
            return is_left and is_right
            
        
        return dfs(p, q)