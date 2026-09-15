# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        p1 = head
        if head and head.next:
            p2 = head.next.next
        else:
            return

        while p2 and p2.next:
            if p1:
                p1 = p1.next
            if p2 and p2.next:
                p2 = p2.next.next
            
        
        p2 = p1.next
        p1.next = None
        p1 = head

     
        #reverse
        prev = None

        while p2:
            temp = p2.next
            p2.next = prev
            prev = p2
            p2 = temp
        # print(p1.next.val)
        # print(prev.val)

        while p1:
             temp = p1.next
             p1.next = prev
             p1 = temp
             if p1 and prev:
                temp = prev.next
                prev.next = p1
                prev = temp
        return