class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        q = collections.deque()
        ROW, COL = len(grid), len(grid[0])
        visited = set()

        def bfs(i, j):
            visited.add((i,j))
            while q:
                n = q.popleft()
                directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = n[0] + dr, n[1] + dc
                    if (r in range(ROW) and c in range(COL)) and grid[r][c] == "1" and (r,c) not in visited:
                        q.append([r,c])
                        visited.add((r,c))
        ans = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    q.append([i,j])
                    bfs(i, j)
                    ans += 1
        return ans
