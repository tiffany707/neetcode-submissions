# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maximum = 0
        
        def recursion(root):
            if root == None:
                return -1
            left = recursion(root.left) + 1
            right = recursion(root.right) + 1
            print("val", root.val)
            print("left", left)
            print("right", right)
            if left + right > self.maximum:
                self.maximum = left + right
            print(self.maximum)
            return max(left, right)
        
        recursion(root)
        return self.maximum