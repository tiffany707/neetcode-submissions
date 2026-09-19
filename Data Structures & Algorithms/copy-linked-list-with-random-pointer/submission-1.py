"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        lookup = {}
        dummy = Node(0)
        curr = dummy
        temp = head
        while head:
            n = Node(head.val, None, None)
            lookup[head] = n
            curr.next = n
            curr = curr.next
            head = head.next
        
        curr = dummy.next
        head = temp
        while head:
            if head.random != None:
                curr.random = lookup[head.random]
            curr = curr.next
            head= head.next
        return dummy.next

