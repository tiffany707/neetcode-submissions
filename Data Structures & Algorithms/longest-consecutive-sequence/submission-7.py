class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set(nums)
        ans = 0
        for n in lookup:
            if n - 1 not in lookup:
                count = 1
                ans = max(ans, count)
                while n + 1 in lookup:
                    count += 1
                    ans = max(ans, count)
                    n += 1

        return ans
