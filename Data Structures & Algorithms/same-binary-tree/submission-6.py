# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.answer = True
        if not p and not q:
            return self.answer
        elif not p or not q:
            self.answer = False
            return self.answer 
        L = self.isSameTree(p.left, q.left)

        R = self.isSameTree(p.right, q.right)

        if p.val != q.val:
            self.answer = False
            return self.answer
        else:
            if L and R:
                return True
            else:
                return False



