class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        aM = collections.defaultdict(list)
        iD = [0] * numCourses

        for u, v in prerequisites:
            iD[u] += 1 
            aM[v].append(u)

        q = collections.deque([i for i in range(len(iD)) if iD[i] == 0])
        ans = 0
        while q:
            n = q.popleft()
            ans += 1
            for nei in aM[n]:
                iD[nei] -= 1
                if iD[nei] == 0:
                    q.append(nei)
        return ans == numCourses

            

