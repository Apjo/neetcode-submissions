# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = list1, list2
        dummy = ListNode(-999)
        temp = dummy
        if not list1 and list2:
            return list2
        if not list2 and list1:
            return list1

        while p1 is not None and p2 is not None:
                if p1.val <= p2.val:
                    temp.next = p1
                    p1=p1.next
                else:
                    temp.next = p2
                    p2=p2.next
                temp=temp.next
        while p1 is not None:
            temp.next = p1
            p1=p1.next
            temp=temp.next
        while p2 is not None:
            temp.next = p2
            p2=p2.next
            temp=temp.next
        return dummy.next