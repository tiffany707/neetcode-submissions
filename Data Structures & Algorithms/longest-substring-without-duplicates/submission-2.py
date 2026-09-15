class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        mySet = set()
        res = 0

        for i in range(len(s)):
            while s[i] in mySet:
                mySet.remove(s[l])
                l += 1
            mySet.add(s[i])
            res = max(res, i - l + 1)
        return res

        