class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        ans = []
        
        #left
        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]
        
        #right
        for i in range(len(nums) - 2, -1, -1):
            right[i] = right[i+1] * nums[i + 1]

        #ans
        for i in range(len(nums)):
            ans.append(right[i] * left[i])
        
        return ans
        # ans = []
        # [1,2,4,6]
        # [1,1,2,8]
        # [48,24,6,1]