import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums) + 1)]
        lookup = {}
        for n in nums:
            lookup[n] = 1 + lookup.get(n, 0)

        for key, value in lookup.items():
            bucket[value].append(key)

        ans = []
        for i in range(len(bucket) - 1, -1 , -1):
            if bucket[i]:
                for n in bucket[i]:
                    ans.append(n)
                    if len(ans) == k:
                        return ans


            