from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
            my_set = set()
            for key in nums:
                if key in my_set:
                    return True
                my_set.add(key)
            return False
  
