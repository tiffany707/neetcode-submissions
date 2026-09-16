class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lookup = collections.Counter(nums)
        for val in lookup.values():
            if val > 1:
                return True
        return False