# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class NodeWrap:
    def __init__(self, n):
        self.node = n

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #dump all into a priority queue
        min_h = []
        #add all items to min heap
        if not lists:
            return None
        for item in lists:
            if item is not None:
                heapq.heappush(min_h, NodeWrap(item))
        
        dummy=ListNode(-999)
        curr=dummy
        #pop from the min heap, and start appending to a new list
        while min_h:
            popped = heapq.heappop(min_h)
            #append this node to the next of curr
            curr.next = popped.node
            curr=curr.next
            #if the popped node has a next, add to the min heap
            if popped.node.next:
                heapq.heappush(min_h, NodeWrap(popped.node.next))

        return dummy.next