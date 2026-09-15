from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary = {}

        if len(s) != len(t):
            return False
        
        for l in s:
            if l in dictionary:
                dictionary[l] += 1
            else:
                 dictionary[l] = 1
        
        for l in t:
            if l in dictionary:
                dictionary[l] -= 1
                if dictionary [l] < 0:
                    return False
            else:
                return False
            
        return True
            
