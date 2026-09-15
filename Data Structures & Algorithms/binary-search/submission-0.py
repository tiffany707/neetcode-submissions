class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        middle = (right + left) // 2 

        if target > nums[right]:
            return -1
        elif target < nums[left]:
            return -1

        if nums[right] == target:
            return right
        elif nums[left] == target: 
            return left

        while middle != right and middle != left:
            if nums[middle] == target:
                return middle
            else:
                if nums[middle] > target:
                    right = middle 
                    middle = (right + left) //2
                else:
                    left = middle
                    middle = (right + left) //2
        return -1

        
        