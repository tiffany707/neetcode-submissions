class Solution:
    def rob(self, nums: List[int]) -> int:
        lookup = {}

        def rec(x):
            if x in lookup:
                return lookup[x]
            if x >= len(nums):
                return 0 
            res = max(rec(x + 2), rec (x + 3)) + nums[x]
            lookup[x] = res
            return  res

        one = rec(0)
        two = rec(1)
        return max(one, two)
