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
        time = []

        for i in intervals:
            time.append([i.start, +1])
            time.append([i.end, -1])
        
        time.sort(key=lambda x: (x[0], x[1]))
        ans = 0
        curr = 0
        for i in range(len(time)):
            curr += time[i][1]
            ans = max(ans, curr)

        return ans


