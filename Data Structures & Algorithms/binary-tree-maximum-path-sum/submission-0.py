# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #l + root + r
        #root
        self.ans = root.val
        def rec(n):
            if not n:
                return 0
            l = max(0, rec(n.left))
            r = max(0, rec(n.right))
            total = l + r + n.val
            self.ans = max(self.ans, total)
            return max(l, r) + n.val

        rec(root)
        return self.ans

            