class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = 1, 1
        ans = max(nums)

        for n in nums:
            if n == 0:
                curMax, curMin = 1, 1
            temp = curMax
            curMax = max(n, n * curMax, n * curMin)
            curMin = min(n, n * temp, n * curMin)
            ans = max(curMax, ans)

        return ans
