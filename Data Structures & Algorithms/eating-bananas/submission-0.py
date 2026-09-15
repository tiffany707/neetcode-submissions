import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1 
        r = max(piles)
        answer = max(piles)

        while l <= r:
            m = (l + r) // 2 
            temp = h
            for key in piles:
                temp -= math.ceil(key / m)
                if math.ceil(key / m) == 0:
                    temp -= 1
            if m < answer and temp >= 0:
                answer = m


            #shifting l & r
            if temp >= 0:
                r = m - 1
            else:
                l = m + 1

        return answer


        