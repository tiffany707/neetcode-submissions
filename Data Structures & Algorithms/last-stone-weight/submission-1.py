import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)

        def recurse(stones):
            if len(stones) == 0:
                return 0
            if len(stones) == 1:
                return -heapq.heappop(stones)
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if first > second:
                val = second - first
            else:
                val = first - second
            heapq.heappush(stones, val)
            return recurse(stones)

        return recurse(stones)