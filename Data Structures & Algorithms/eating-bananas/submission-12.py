class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calc(m):
            nonlocal h
            hour = h
            for p in piles:
                hour -= math.ceil(p / m)
                if hour < 0:
                    return False
            return True

        ans = max(piles)
        l = 1
        r = ans

        while l <= r:
            m = (l+r) // 2
            finished = calc(m)
            if finished:
                ans = min(ans, m)
                r = m - 1
            else:
                l = m + 1

        return ans



    