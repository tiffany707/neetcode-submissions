import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.arr = []
        self.largest = k
        for key in nums:
            heapq.heappush(self.arr, -key)

    def add(self, val: int) -> int:
        heapq.heappush(self.arr, -val)
        copyArr = self.arr[:]
        print(copyArr)
        for i in range(self.largest):
            val = heapq.heappop(copyArr)
        return -val
       

