class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lookup  = {}
        ans = 1

        def rec(x, prev):
            if x in lookup:
                return lookup[x]
            if x >= len(nums):
                return 0
            if nums[x] <= prev:
                return 0
            
            res = 0
            for i in range(x + 1, len(nums)):
                res = max(res, rec(i, nums[x]))
            lookup[x] = res + 1
            print(x, res + 1)
            return res + 1


        
        for x in range(len(nums)):
           ans = max(ans, rec(x, -1001))
        return ans
        