from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictionary = defaultdict(int)
        
        for n in nums:
            if dictionary[n] == 1:
                return True
            else:
                dictionary[n] = 1
        return False
        