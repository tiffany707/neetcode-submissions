# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            current = head.next
        else:
            return
        myList = ListNode(head.val)
        newNode = myList

        
        while current:
            newNode = ListNode(current.val, myList)
            current = current.next
            myList = newNode

        return newNode
            
        