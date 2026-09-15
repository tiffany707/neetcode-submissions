class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        max = 0

        for key in prices:
            if key < min:
                min = key
            if key - min > max:
                max = key - min
        
        return max 
                



        