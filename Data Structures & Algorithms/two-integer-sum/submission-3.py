from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = defaultdict(int)

        for i in range(len(nums)):
            pair = target - nums[i]
            if pair in dictionary:
                return [dictionary[pair], i]
            else:
                dictionary[nums[i]] = i

        