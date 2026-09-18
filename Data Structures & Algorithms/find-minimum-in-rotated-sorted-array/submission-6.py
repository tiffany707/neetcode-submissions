class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
     

            if nums[r] >= nums[m] and nums[r] >= nums[l]:
                return nums[l]
            elif nums[r] >  nums[m] and nums[r] < nums[l]:
                r = m
            else:
                l = m + 1
        return -1