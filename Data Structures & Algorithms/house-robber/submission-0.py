class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        cache = [-1] * len(nums)

        def dfs(i):
            if i >= len(nums):
                return 0
            if cache[i] != -1:
                return cache[i]
            total = max(dfs(i + 2), dfs(i+3))
            cache[i] = total + nums[i]
            return total + nums[i]
        dfs(0)
        dfs(1)
        return max(cache[0], cache[1])