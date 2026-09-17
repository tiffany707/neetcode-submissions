class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxL = 0
        maxR = 0
        ans = 0

        while l < r:
            if min(maxL, maxR) - min(height[l], height[r]) > 0:
                ans += min(maxL, maxR) - min(height[l], height[r])
            maxL = max(maxL, height[l])
            maxR = max(maxR, height[r])
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ans

        
