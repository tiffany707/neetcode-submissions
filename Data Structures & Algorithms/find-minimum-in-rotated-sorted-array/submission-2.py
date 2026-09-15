class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        answer = float('inf')

        while l <= r:
            m = (l + r) // 2

            if nums[m] < nums[r]:
                r = m - 1
            else:
                l = m + 1
            answer = min(answer, nums[m], nums[r])
        return answer
