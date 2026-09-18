class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i in range(len(heights)):
            if not stack or (stack and heights[i] >= stack[-1][1]): 
                stack.append([i, heights[i]])
            else:
                finalIndex = 0
                while stack and stack[-1][1] > heights[i]:
                    p = stack.pop()
                    maxArea = max(maxArea, (i - p[0]) * p[1])
                    finalIndex = p[0]
                stack.append([finalIndex, heights[i]])

        if stack:
            while stack:
                    p = stack.pop()
                    maxArea = max(maxArea, (len(heights) - p[0]) * p[1])
        return maxArea