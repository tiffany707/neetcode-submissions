class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        lookup = defaultdict(list)
        ans = float('inf')

        def rec(total):
            if total in lookup:
                return lookup[total]
            if total < 0:
                return float('inf')
            if total == 0:
                return 0
            small = float('inf') 
            for x in range(len(coins)):
                small = min(small, rec(total - coins[x]))
            lookup[total] = small + 1
            return small + 1
        ans = rec(amount)
        if ans == float('inf'):
            return -1 
        else:
            return ans 