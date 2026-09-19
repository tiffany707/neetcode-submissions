# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
        dummy = ListNode()
        while len(lists) > 1:
            tempList = []
            for i in range(0, len(lists), 2):
                p1 = lists[i]
                p2 = lists[i + 1] if i + 1 < len(lists) else None

                curr = dummy
                while p1 and p2:
                    if p1.val > p2.val:
                        curr.next = p2
                        p2 = p2.next
                    else:
                        curr.next = p1
                        p1 = p1.next
                    curr = curr.next
                curr.next = p1 or p2
                tempList.append(dummy.next)
            lists = tempList

        return lists[0]

