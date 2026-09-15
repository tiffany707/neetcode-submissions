class Solution:
    def numDecodings(self, s: str) -> int:
       lookup = {len(s): 1}

       def rec(i):
            if i in lookup:
                return lookup[i]
            if s[i] == "0":
                return 0
            
            res = rec(i + 1)
            if i + 2 <= len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                res += rec(i + 2)
            lookup[i] = res
            return res

       return rec(0)