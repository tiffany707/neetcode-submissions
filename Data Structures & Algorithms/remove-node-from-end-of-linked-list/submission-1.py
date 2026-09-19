# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        p2 = dummy
        for i in range(n+1):
            p2 = p2.next
        
        curr = dummy
        while p2:
            curr = curr.next
            p2 = p2.next
        
        curr.next = curr.next.next
        return dummy.next
            