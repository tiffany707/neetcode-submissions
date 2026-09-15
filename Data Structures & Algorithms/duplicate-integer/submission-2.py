from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictionary = defaultdict(int)
    
        for key in nums:
            dictionary[key] += 1
            if dictionary[key] >= 2:
                return True
        return False
  
