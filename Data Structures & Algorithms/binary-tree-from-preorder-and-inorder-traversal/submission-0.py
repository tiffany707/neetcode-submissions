# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        lookup = {val:key for key, val in enumerate(inorder)}
        count = 0

        def rec(n, i, j):
            nonlocal count
            if n >= len(preorder):
                return None
            if i > j:
                return None
            count += 1
            root = TreeNode(preorder[n])
            index = lookup[preorder[n]]
            root.left = rec(count, i, index - 1)
            root.right = rec(count, index + 1, j)
            return root
        
        return rec(0, 0, len(inorder)-1)

        