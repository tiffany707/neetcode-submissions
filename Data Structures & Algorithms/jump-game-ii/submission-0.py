class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        l, r = 0, 0

        while r < len(nums) - 1:
            greatest = r
            for i in range(l, r + 1):
                greatest = max(greatest, nums[i] + i)
            l = r + 1 
            r = greatest
            count += 1
        
        return count

