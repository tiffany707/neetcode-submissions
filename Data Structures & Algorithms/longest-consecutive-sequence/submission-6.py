import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)
        maximum = 0
        while mySet:
            temp = min(mySet)
            count = 1
            flag = False

            while not flag:
                if temp + 1 in mySet:
                    mySet.remove(temp)
                    temp = temp + 1
                    count += 1
                else:
                    if count > maximum:
                        maximum = count
                    mySet.remove(temp)
                    flag = True
                print(mySet)
        return maximum