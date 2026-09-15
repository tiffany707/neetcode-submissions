class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        answer = float('inf')

        while l <= r:
            print(nums[l])
            print(l)
            print(r)
            print("r",nums[r])
            m = (l + r) // 2
            print(m)
            border = min(nums[l], nums[r], nums[m])
            print("b", border)
            if border < answer:
                answer = border
            if border == nums[l] or border == nums[r]:
                l = m + 1
            elif border == nums[m]:
                r = m - 1
        return answer
