class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = (numbers[len(numbers) - 1], len(numbers) - 1)
        p2 = (numbers[0], 0)
        while True:
            print(p1)
            print(p2)
            if p1[0] + p2[0] > target:
                p1 = (numbers[p1[1]-1], p1[1]-1)
            elif p1[0] + p2[0] < target:
                p2 = (numbers[p2[1]+1], p2[1]+1)
            else:
                return [p2[1]+1, p1[1]+1]
        