class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        lookup = {}

        def rec(i, j):
            if (i, j) in lookup:
                return lookup[(i, j)]
            if i == m-1 and j == n - 1:
                return 1
            if i >= m or j >= n:
                return 0
            ans =  rec(i + 1, j) + rec(i, j + 1)
            lookup[(i, j)] = ans
            return ans 
            
        
        return rec(0,0)