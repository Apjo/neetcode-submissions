# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        bfs_q = deque([root])
        res=""
        while bfs_q:
            curr = bfs_q.popleft()
            if not curr:
                res+="#,"
                continue
           
            res+=str(curr.val)+","
            bfs_q.append(curr.left)
            bfs_q.append(curr.right)
        # print(f"returning serialized tree as={res}")
        return res


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data or data == "":
            return None
        bfs_q = deque()
        formatted_data = data.split(",")
        print(f"stringified tree={formatted_data}, with len={len(formatted_data)}")
        curr_root = TreeNode(int(formatted_data[0]))
        bfs_q.append(curr_root)
        i=1
        while bfs_q:
            
            # for i in range(1, len(formatted_data)):
                print(f"i at={i}")
                curr = bfs_q.popleft()
                print(f"data at i={formatted_data[i]}")
                if formatted_data[i] != '#':
                    left_child = TreeNode(int(formatted_data[i]))
                    curr.left = left_child
                    bfs_q.append(left_child)
                i+=1
                if formatted_data[i] != '#':
                    right_child = TreeNode(int(formatted_data[i]))
                    curr.right = right_child
                    bfs_q.append(right_child)
                i+=1
        return curr_root