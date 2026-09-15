class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right= [0] * len(nums)
        left= [0] *len(nums)
        right[len(nums) - 1] = nums[-1]
        left[0] = nums[0]

        #left 
        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i]

        #right
        for i in range(len(nums) - 2, -1 ,-1):
            right[i] = right[i + 1] * nums[i]
        
        ans = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                ans[0] = right[i + 1]
            elif i == len(nums) - 1:
                ans[len(nums) - 1] = left[i - 1]
            else:
                ans[i] = right[i + 1] * left[i - 1]
        return ans
