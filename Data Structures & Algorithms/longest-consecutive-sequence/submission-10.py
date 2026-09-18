class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        lookup = set(x for x in nums)

        for n in lookup:
            if n - 1 not in lookup:
                count = 1
                while n + 1 in lookup:  
                    count += 1
                    n += 1
                ans =max(ans, count)
        return ans