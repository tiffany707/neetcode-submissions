class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        def ts(edges):
            aL = collections.defaultdict(list)
            inDegree = collections.defaultdict(int)
            nodes = set()
            for u, v in edges:
                if u not in inDegree:
                    inDegree[u] = 0
                inDegree[v] += 1
                aL[u].append(v)
                nodes.add(u)
                nodes.add(v)

            q = collections.deque([node for node in inDegree.keys() if inDegree[node] == 0])
            endList = []
            while q:
                n = q.popleft()
                endList.append(n)
                for neighbor in aL[n]:
                    inDegree[neighbor] -= 1
                    if inDegree[neighbor] == 0:
                        q.append(neighbor)
            if len(endList) == len(nodes):
                return True
            return False
        return ts(prerequisites)
            

