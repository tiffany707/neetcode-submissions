class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
                nums2 = nums.copy()
                for key in nums:
                    nums2.pop(0)
                    print(nums)
                    for key2 in nums2:
                        if key == key2:
                            print(key)
                            print(nums)
                            return True
        return False
