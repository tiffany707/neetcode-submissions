class Solution:
    def climbStairs(self, n: int) -> int:
        lookup = {}

        def rec(x):
            if x in lookup:
                return lookup[x]
            if (x == 0):
                return 1
            if x < 0:
                return 0
            ans = rec(x - 1) + rec(x - 2)
            lookup[x] = ans
            return ans
        

        return rec(n)
           

            