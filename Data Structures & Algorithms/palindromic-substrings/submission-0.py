class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def rec(l, r):
            nonlocal count
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1 
                count += 1
        
        for x in range(len(s)):
            rec(x, x)
            rec(x, x + 1)
        return count
            
