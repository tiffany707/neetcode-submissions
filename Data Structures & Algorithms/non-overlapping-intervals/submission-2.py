class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ans = 0
        curr = intervals[0]
        i = 1
        while i < len(intervals):
            if curr[1] > intervals[i][1]:
                curr = intervals[i]
                ans += 1
            elif curr[1] <= intervals[i][0]:
                curr = intervals[i]
            else:
                ans += 1
            i += 1

        return ans

