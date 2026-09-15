from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for key in nums:
            dic[key] += 1
        
        list = [(-value, key) for key, value in dic.items()]
        heapq.heapify(list)

        answer = []
        for i in range(k):
            val = heapq.heappop(list)
            answer.append(val[1])
        return answer



        