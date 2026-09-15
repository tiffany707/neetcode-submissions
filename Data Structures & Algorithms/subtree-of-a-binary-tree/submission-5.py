# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def search(root, subRoot):
            if not root:
                return False
           
            if root.val == subRoot.val:
                return recurse(root, subRoot) or search(root.right, subRoot) or search(root.left, subRoot)
            else:
                return search(root.right, subRoot) or search(root.left, subRoot)

        def recurse(root, subRoot):
            if not root and not subRoot:
                return True
            if (not subRoot and root) or (not root and subRoot) or root.val != subRoot.val:
                return False
            
          
            return recurse(root.left, subRoot.left) and recurse(root.right, subRoot.right)

        return search(root, subRoot)