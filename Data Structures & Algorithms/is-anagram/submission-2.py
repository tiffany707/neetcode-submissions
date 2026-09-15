from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary = defaultdict(int)

        if len(s) != len(t):
            return False
        
        for l in s:
            dictionary[l] += 1
        
        for l in t:
            dictionary[l] -= 1
            if dictionary [l] < 0:
                return False
            
        return True
            
