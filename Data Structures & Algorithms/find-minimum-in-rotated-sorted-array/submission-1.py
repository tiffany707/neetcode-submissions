class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        answer = float('inf')

        while l <= r:
            m = (l + r) // 2
            border = min(nums[l], nums[r], nums[m])
            if border < answer:
                answer = border
            if border == nums[l] or border == nums[r]:
                l = m + 1
            elif border == nums[m]:
                r = m - 1
        return answer
