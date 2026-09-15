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
        nums = []

        for i in intervals:
            if nums and i.start >=  nums[0]:
                heapq.heappop(nums)
                heapq.heappush(nums, i.end)
            else:
                heapq.heappush(nums, i.end)
        return len(nums)
