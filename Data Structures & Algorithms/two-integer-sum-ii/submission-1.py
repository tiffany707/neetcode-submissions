class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lookup = {}
        for i in range(len(numbers)):
            targetNum = target - numbers[i]
            if targetNum in lookup:
                return [lookup[targetNum] + 1, i+ 1]
            else:
                lookup[numbers[i]] = i