import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lookup = collections.Counter(nums)
        minh = []

        for key, value in lookup.items():
            heapq.heappush(minh, (value, key))
            if len(minh) > k:
                heapq.heappop(minh)
        
        ans = []
        for n in minh:
            ans.append(n[1])
        return ans