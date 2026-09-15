# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.arr1 = []
        self.arr2 = []

        def dfs1(root):
            if root == None:
                self.arr1.append(-100)
                return
            left = dfs1(root.left)
            right = dfs1(root.right)
            self.arr1.append(root.val)

        def dfs2(root):
            if root == None:
                self.arr2.append(-100)
                return
            left = dfs2(root.left)
            right = dfs2(root.right)
            self.arr2.append(root.val)
        
        
        dfs1(p)
        dfs2(q)

        if self.arr1 == self.arr2:
            return True
        return False
