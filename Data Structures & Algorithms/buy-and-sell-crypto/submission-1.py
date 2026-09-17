class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        minValue = 101
        for n in prices:
            ans = max(n - minValue, ans)
            minValue = min(minValue, n)
        return ans