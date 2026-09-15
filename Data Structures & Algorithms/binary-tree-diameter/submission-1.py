# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def recurse(root):
            if root is None:
                return -1
            l = recurse(root.left) + 1 
            r = recurse(root.right) + 1
            self.res = max((l+r), self.res)

            return max(l,r)

        recurse(root)
        return self.res