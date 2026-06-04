# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        if not root:
            return res
        bfs_q = deque()
        bfs_q.append(root)
        #res.add([root.val])
        while bfs_q:
            N = len(bfs_q)
            temp=[]

            for i in range(N):
                curr = bfs_q.popleft()
                temp.append(curr.val)
                if curr.left:
                    #temp.append(curr.left.val)
                    bfs_q.append(curr.left)
                if curr.right:
                    #temp.append(curr.right.val)
                    bfs_q.append(curr.right)
            if temp:
                res.append(temp)
        return res