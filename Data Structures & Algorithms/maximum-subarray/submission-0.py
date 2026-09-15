class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = max(nums)
        curr = 0
        for i in range(len(nums)):
            if curr + nums[i] < 0:
                curr = 0
            else:
                curr += nums[i]
            if not(ans < 0 and curr == 0):
                ans = max(ans, curr)
        return ans