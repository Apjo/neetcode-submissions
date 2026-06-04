# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
        def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
            #get root index which will always be pre[0], and this will be the root of the tree
            #num Nodes on left of root index in the inorder will be responsible for left subtree
            # everything to the right of the root index in the inorder traversal will be responsible for the right subtree
            #recurse
            def solve(pre_st, pre_end, ino_st, ino_end):
                if pre_st > pre_end or ino_st > ino_end:
                    return None
                #create root node from preorder
                root_node = TreeNode(preorder[pre_st])
                #determine index of root in inorder traversal
                i, root_idx_ino = ino_st, ino_st
                
                while i <= ino_end:
                    if inorder[i] == root_node.val:
                        root_idx_ino = i
                        break
                    i+=1
                #calculate number of nodes in the left subtree
                num_nodes_on_left = root_idx_ino - ino_st
                
                root_node.left = solve(pre_st + 1, pre_st + num_nodes_on_left, ino_st, ino_end)
                root_node.right = solve(pre_st+num_nodes_on_left + 1, pre_end, root_idx_ino + 1, ino_end)

                return root_node

            return solve(0, len(preorder) - 1, 0, len(inorder) - 1)