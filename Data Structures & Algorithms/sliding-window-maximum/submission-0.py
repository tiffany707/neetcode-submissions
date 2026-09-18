import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxH = []
        output = []

        for i in range(len(nums)):
            heapq.heappush(maxH, (-nums[i], i))
            if len(maxH) >= k:
                while maxH[0][1] <= i - k:
                    heapq.heappop(maxH)
                output.append(-maxH[0][0])
        return output