# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root is None:
                return [True, 0] 
            
            l = dfs(root.left)
            r = dfs(root.right)

            if abs(l[1]-r[1]) > 1:
                return [False, 0]
            
            return [l[0] and r[0], max(r[1], l[1]) + 1]
            
        return dfs(root)[0]
        


        