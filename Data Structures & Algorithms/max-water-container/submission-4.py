class Solution:
    def maxArea(self, heights: List[int]) -> int:
        answer = 0
        ml = (0,0)
        mr = (0,0)
        l = (heights[0], 0)
        r = (heights[len(heights)-1], len(heights) - 1)

        while l[1] < r[1]:
            currArea = min(l[0], r[0]) * (r[1] - l[1])
            currLeft = min(ml[0], r[0]) * (r[1] - ml[1])
            currRight = min(mr[0], l[0]) * (mr[1] - l[1])
            if currArea > answer:
                print(currArea)
                answer = currArea
                ml = (l)
                mr = (r)
            elif currLeft > answer:
                print(currLeft)
                answer = currLeft
                mr = r
                ml = l
            elif currRight > answer:
                print(currRight)
                answer = currRight
                mr = r
                ml = l
            
            if l[0] + len(heights) - l[1] > r[0] +  r[1]:
                r = (heights[r[1]-1], r[1] - 1)
            else:
                l = (heights[l[1]+1], l[1] + 1)
        return answer
            
        