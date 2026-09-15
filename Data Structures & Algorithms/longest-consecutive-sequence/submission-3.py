import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        heapq.heapify(nums)
        if nums == []:
            return 0
        max = 0
        count = 1
        temp = heapq.heappop(nums)
        x = len(nums)
        for i in range(x):
            val = heapq.heappop(nums)
            if temp + 1 == val:
                count += 1
            elif temp == val:
                pass
            elif count > max:
                max = count
                count = 1
            else:
                count = 1
            temp = val
        if count > max:
                max = count
        return max