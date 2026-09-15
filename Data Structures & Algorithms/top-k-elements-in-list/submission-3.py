from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        bucket = [[] for x in range(len(nums) + 1) ]

        for key, value in count.items():
            bucket[value].append(key)

        res = []
        for i in range(len(nums), 0, -1):
            for j in bucket[i]:
                res.append(j)
                k -= 1
                if k ==0:
                    return res
        return res
        