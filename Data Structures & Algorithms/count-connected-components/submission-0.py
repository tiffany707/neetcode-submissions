class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.parent = [x for x in range(n)]
        self.rank = [1] * n

        def find(n):
            curr = n
            
            while curr != self.parent[curr]:
                self.parent[curr] = self.parent[self.parent[curr]]
                curr = self.parent[curr]
            return curr
        
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2:
                return 0

            if self.rank[p1] > self.rank[p2]:
                self.parent[p2] = p1
                self.rank[p1] += self.rank[p2]
            else:
                self.parent[p1] = p2
                self.rank[p2] += self.rank[p1]
            
            return 1

        self.ans = n
        for u, v in edges:
            self.ans -= union(u, v)
        return self.ans
