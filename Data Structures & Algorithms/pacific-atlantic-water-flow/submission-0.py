class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(i, j, path, nums):
            if (i, j) in path or i < 0 or j < 0 or i >= ROWS or j >= COLS or nums > heights[i][j]:
                return
            path.add((i, j))
            dfs(i + 1, j, path, heights[i][j])
            dfs(i - 1, j, path, heights[i][j])
            dfs(i, j + 1, path, heights[i][j])
            dfs(i, j - 1, path, heights[i][j])
        
        for i in range(ROWS):
            dfs(i, 0, pacific, 0)
            dfs(i, COLS - 1, atlantic, 0)
        
        for j in range(COLS):
            dfs(0, j, pacific, 0)
            dfs(ROWS - 1, j, atlantic, 0)
        
        res = []

        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) in pacific and (i,j) in atlantic:
                    res.append([i, j])

        return res
        

       













