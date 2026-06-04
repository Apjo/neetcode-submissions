# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head
        
        temp,slow, fast = ListNode(-999, head), head,head
        slow=temp
        if head.next is None and n==1:
            return None
        for i in range(n):
            fast=fast.next

        while fast:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return temp.next
        