# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        slow,fast = head, head
        while fast is not None and fast.next is not None:
            fast=fast.next.next
            slow=slow.next
        def reverse(n):
            curr = n
            prev, nxt = None, None
            while curr is not None:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        head2 = reverse(slow.next)
        slow.next = None
        while head is not None and head2 is not None:
            n1 = head.next
            n2 = head2.next
            head.next = head2
            head2.next = n1
            head=n1
            head2=n2