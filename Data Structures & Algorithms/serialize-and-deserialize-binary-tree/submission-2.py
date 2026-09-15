# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.ans = ""
        self.q = collections.deque()
        self.q.append(root)
        while self.q:
            n = self.q.popleft()
            if not n:
                self.ans += 'N/'
                continue
            else:
                self.ans += str(n.val) + '/'

                l = n.left
                r = n.right
                self.q.append(l)
                self.q.append(r)
        print(self.ans)
        return self.ans




        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split("/")
        q = collections.deque()
        if data[0] == 'N':
            return None
        root = TreeNode(int(data[0]))
        q.append(root)

        i = 1
        while q and i < len(data):
            n = q.popleft()
            
            if data[i] != 'N':
                n.left = TreeNode(int(data[i]))
                q.append(n.left)
            
            i += 1

            if data[i] != 'N':
                n.right = TreeNode(int(data[i]))
                q.append(n.right)
            
            i += 1
        
        return root

