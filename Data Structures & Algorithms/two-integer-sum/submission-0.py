class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}

        for i in range(len(nums)):
            
            dictionary[nums[i]] = dictionary.get(nums[i], []) 
            dictionary[nums[i]].append(i)

        for key in nums:
            x = target - key
            
            if len(dictionary[key]) > 1:
                index = dictionary[key][1]
            else:
                index = dictionary[key][0] 
            
            if x in dictionary and index != dictionary[x][0]:
                if index < dictionary[x][0]:
                    return [index, dictionary[x][0]]
                else:
                    return [dictionary[x][0], index]
            