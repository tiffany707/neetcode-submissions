class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lookup = collections.defaultdict(int)
        l = 0
        maxFreq = 0
        ans = 0
        
        for i in range(len(s)):
            lookup[s[i]] += 1
            maxFreq = max(maxFreq, lookup[s[i]])
            if i - l + 1 - maxFreq <= k:
                ans = max(ans, i - l + 1)
            else:
                lookup[s[l]] -= 1
                l += 1
        return ans