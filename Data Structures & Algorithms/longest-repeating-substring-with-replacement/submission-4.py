from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        myDict = defaultdict(int)

        for i in range(len(s)):
            myDict[s[i]] += 1
            while i-l+1 -max(myDict.values()) > k:
                print(i-l+1)
                print(myDict[s[l]])
                print(s[i])
                myDict[s[l]] -= 1
                l += 1
            res = max(res, i-l+1)
        return res
            
            
        