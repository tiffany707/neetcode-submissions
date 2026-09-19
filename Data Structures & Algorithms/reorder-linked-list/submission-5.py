# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 
        
        p1 = head
        p2 = head.next
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
        
        #reverse
        p = p1.next
        p1.next = None
        prev = None 
        while p:
            temp = p.next
            p.next = prev
            prev = p
            p = temp

        #merge
        dummy = ListNode()
        curr = dummy
        p1 = head
        p2 = prev

        while p1 and p2:
            curr.next = p1
            p1 = p1.next
            curr = curr.next
            curr.next = p2
            p2 = p2.next
            curr = curr.next
        if p1:
            curr.next = p1
