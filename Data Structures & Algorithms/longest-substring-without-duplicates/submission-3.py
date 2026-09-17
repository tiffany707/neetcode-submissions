class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup = collections.defaultdict(int)
        l = 0
        ans = 0
        for r in range(len(s)):
            lookup[s[r]] += 1
            if lookup[s[r]] > 1:
                while l < r and lookup[s[r]] > 1:
                    lookup[s[l]] -= 1
                    l += 1
            else:
                ans = max(ans, r - l + 1)
        return ans
