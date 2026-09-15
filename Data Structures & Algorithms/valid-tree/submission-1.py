class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        adj = {x: [] for x in range(n)}

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        def dfs(n, prev):
            if n in visited:
                return False
            
            visited.add(n)
            for neigh in adj[n]:
                if neigh != prev:
                    if not dfs(neigh, n):
                        return False
            
            return True


        return dfs(0, -1) and len(visited) == len(adj)
