# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.answer = True
        def recursion(node):
            if node == None:
                return 0
            print(node.val)
            left = recursion(node.left) + 1
            right = recursion(node.right) + 1
            if left - right > 1 or right - left > 1:
                self.answer = False
            return max(left, right)
        recursion(root)
        return self.answer

        