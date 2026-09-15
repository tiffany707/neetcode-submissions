
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#nlr pre
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root != None:
            print(root.val)
            temp = root.left
            self.invertTree(root.left)
            root.left = root.right
            self.invertTree(root.left)
            root.right = temp
        return root