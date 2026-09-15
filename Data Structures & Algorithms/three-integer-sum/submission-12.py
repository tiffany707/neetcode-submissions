class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answers = []
        for i, v in enumerate(nums):
            if v == nums[i-1] and i != 0:
                continue
            p1 = i+1
            p2 = len(nums) - 1
            while p1<p2:
                print(v)
                if nums[p1] + nums[p2] == -v:
                    answers.append([nums[p1], nums[p2], v])
                    p2 = p2-1
                    while nums[p2+1] == nums[p2] and p1<p2:
                        p2 = p2-1
                elif nums[p1] + nums [p2] > -v:
                    p2 = p2 - 1
                else:
                    p1 = p1 + 1 
        return answers


                


        