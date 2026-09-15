class Solution:
    def minWindow(self, s: str, t: str) -> str:
        targetHash = collections.Counter(t)
        sHash = {}
        for x in t:
            sHash[x] = 0
        need = len(targetHash)
        seen = 0
        minLength = float('inf')
        minString = [-1,-1]
        i = 0
        j = 0
        while j < len(s):
            if s[j] in sHash:
                sHash[s[j]] += 1
                if sHash[s[j]] == targetHash[s[j]]:
                    seen += 1
                    if seen == need:
                        while seen == need:
                            if j - i  + 1< minLength:
                                minLength = j-i + 1
                                minString = [i, j]
                            if s[i] in sHash:
                                sHash[s[i]] -= 1
                                if sHash[s[i]] < targetHash[s[i]]:
                                    seen -= 1
                            i += 1

            j += 1
        
        return s[minString[0]: minString[1] + 1]
                            
                    
