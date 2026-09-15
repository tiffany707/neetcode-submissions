
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictionary = {}
        
        for n in nums:
            if dictionary.get(n) == 1:
                return True
            else:
                dictionary[n] = 1
        return False
        