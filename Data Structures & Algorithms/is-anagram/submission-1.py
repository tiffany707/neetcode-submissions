from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary = defaultdict(int)

        for key in s:
            dictionary[key] +=1
        
        for key in t:
            dictionary[key] -=1
            if dictionary[key] < 0:
                return False
            
        for key in dictionary.values():
            if key > 0:
                return False 

        return True