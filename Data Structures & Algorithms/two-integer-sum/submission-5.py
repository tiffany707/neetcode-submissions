class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i in range(len(nums)):
            look = target - nums[i]
            if look in lookup:
                return [lookup[look], i]
            else:
                lookup[nums[i]] = i