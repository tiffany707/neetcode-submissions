class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        maxH = 0
        minH = 0

        for i in range(len(height)):
            if height[i] >= height[maxH]:
                area = height[maxH] * (i - maxH - 1)
                if area > 0:
                    ans += area - minH
                minH = 0
                maxH = i

            elif height[i] != 0:
                minH += height[i]
        print(maxH)
        temp = maxH
        if minH > 0:
            print("in second part")
            maxH = len(height) - 1
            minH = 0
            for i in range(len(height)-1, temp - 1, -1):
                print(i)
                print(height[i], height[maxH])
                if height[i] >= height[maxH]:
                    area = height[maxH] * (maxH - i - 1)
                    if area > 0:
                        ans += area - minH
                    minH = 0
                    maxH = i

                elif height[i] != 0:
                    minH += height[i]
        
        return ans

        
