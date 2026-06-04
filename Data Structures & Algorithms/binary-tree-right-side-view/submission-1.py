# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        bfs_q = deque()
        res=[]
        if not root:
            return res
        bfs_q.append(root)
        while bfs_q:
            q_len = len(bfs_q)
            for i in range(q_len):
                curr = bfs_q.popleft()
                if i == q_len - 1:
                    res.append(curr.val)
                if curr.left:
                    bfs_q.append(curr.left)
                if curr.right:
                    bfs_q.append(curr.right)
        return res