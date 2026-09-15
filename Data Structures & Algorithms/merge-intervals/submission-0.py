class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        i = 1
        curr = intervals[0]
        while i < len(intervals):
            if curr[1] >= intervals[i][0]:
                curr = [min(curr[0], intervals[i][0]), max(curr[1], intervals[i][1])]
            else:
                ans.append(curr)
                curr = intervals[i]
            i += 1
        ans.append(curr)
        return ans