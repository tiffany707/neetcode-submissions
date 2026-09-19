# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = False
        while l1 or l2 or carry:
            if not l1:
                v1 = 0
            else:
                v1 = l1.val
                l1 = l1.next
            if not l2:
                v2 = 0
            else:
                v2 = l2.val
                l2 = l2.next
            total = v1 + v2
            if carry:
                total += 1
            if total >= 10:
                total -= 10
                carry = True
            else:
                carry = False
            n = ListNode(total)
            curr.next = n
            curr = curr.next
           

        return dummy.next



        