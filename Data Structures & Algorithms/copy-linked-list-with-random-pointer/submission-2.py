"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        from collections import defaultdict
         # returns a new empty node whenever we access a key that doesn't exist yet.
        mp = defaultdict(lambda: Node(0))
        mp[None]=None
        ptr=head
        
        while ptr:
            #get copied node
            copied_node = mp[ptr]
            #set its val
            copied_node.val = ptr.val
            #link its next pointer using the map
            copied_node.next = mp[ptr.next]
            #link its random pointer using the map
            copied_node.random = mp[ptr.random]
            ptr=ptr.next
        return mp[head]
        