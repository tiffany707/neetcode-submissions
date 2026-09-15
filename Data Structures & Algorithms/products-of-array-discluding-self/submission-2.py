class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right = [0] * len(nums)
        left = [0] *len(nums)
        ans = [0] *len(nums)

        left[0] = right[len(nums) - 1] = 1
        #left 
        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]

        #right
        for i in range(len(nums) - 2, -1 ,-1):
            right[i] = right[i + 1] * nums[i + 1]
        
        for i in range(len(nums)):
            ans[i] = left[i] * right[i]
        return ans
