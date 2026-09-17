class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup = {}
        l = 0
        ans = 0
        for r in range(len(s)):
            if s[r] in lookup:
                l = max( l, lookup[s[r]] + 1)
            ans = max(ans, r - l + 1)
            lookup[s[r]] = r
        return ans
