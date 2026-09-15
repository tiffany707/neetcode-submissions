class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n
        def dfs(x):
            if x == n:
                return 1
            elif x > n:
                return 0
            if cache[x] != -1:
                return cache[x]
            
            total = dfs(x + 1) + dfs(x + 2)
            cache[x] = total
            return total
        return dfs(0)
            