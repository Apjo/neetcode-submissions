# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        from collections import deque
        
        if not root:
            return 0
        
        ans=0
        bfs_q = deque()
        bfs_q.append((root, float("-inf")))
        while bfs_q:
            
            curr_node, curr_max = bfs_q.popleft()
            
            if curr_node.val >= curr_max:
                curr_max = curr_node.val
                ans+=1
            
            if curr_node.left:
                bfs_q.append((curr_node.left, curr_max))
            
            if curr_node.right:
                bfs_q.append((curr_node.right, curr_max))

        return ans
        