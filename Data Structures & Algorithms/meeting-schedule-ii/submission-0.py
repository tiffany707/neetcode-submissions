"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: (x.start, x.end))
        nums = [10000001]
        ans = 0

        for i in intervals:
            if i.start >=  nums[0]:
                heapq.heappop(nums)
                heapq.heappush(nums, i.end)
            else:
                ans += 1 
                heapq.heappush(nums, i.end)
        return ans
