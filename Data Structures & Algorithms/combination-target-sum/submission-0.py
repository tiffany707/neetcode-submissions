class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.ans = []
        self.path = []
        def rec(total, i):
            if i > len(nums) - 1 or total > target:
                return 
            if total == target:
                print(total)
                self.ans.append(self.path[:])
                return

            rec(total, i + 1)

            self.path.append(nums[i])
            rec(total + nums[i], i)

            self.path.pop()
        
        rec(0, 0)
        return self.ans
