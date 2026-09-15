# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val <= list2.val:
            main = list1
            alt = list2
        else:
            main = list2
            alt = list1
        isFlag = main
            

        while main.next:
            temp = main.next
            if alt.val <= temp.val:
                main.next = alt
                main = alt
                alt = temp
            else:
                main.next = temp
                main = temp
        
        main.next = alt
                

        return isFlag
        

        
        