from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        bucket = [[] for x in range(len(nums) + 1) ]

        for key in count:
            bucket[count[key]].append(key)

        res = []
        for i in range(len(nums), 0, -1):
            if k == 0:
                return res
            for j in range(len(bucket[i])):
                res.append(bucket[i][j])
                k -= 1
                if k ==0:
                    return res
        return res
        