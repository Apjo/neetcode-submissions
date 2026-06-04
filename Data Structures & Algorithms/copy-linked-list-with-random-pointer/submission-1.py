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
        mp = {None: None}
        curr=head
        while curr is not None:
            mp[curr] = Node(curr.val)
            curr=curr.next
        curr=head
        while curr is not None:
            mp[curr].next = mp[curr.next]# if curr.next else None
            mp[curr].random = mp[curr.random]# if curr.random else None
            curr=curr.next
        return mp[head]