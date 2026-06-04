# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow, fast  = head, head
        # while fast.next is not None:
        #     fast=fast.next
        # if fast.next is None:
        #     return False
        while fast.next is not None:
            fast=fast.next.next
            if fast is None:
                return False
            slow=slow.next
            if fast == slow:
                return True
        return False