import heapq
class MedianFinder:

    def __init__(self):
        self.minh = []
        self.maxh = []

    def addNum(self, num: int) -> None:
        if len(self.minh) == len(self.maxh):
            heapq.heappush(self.maxh, -num)
        else:
            heapq.heappush(self.minh, num)
        
        if self.minh and self.maxh and -(self.maxh[0]) > self.minh[0]:
            minPop = heapq.heappop(self.minh)
            maxPop = heapq.heappop(self.maxh)
            heapq.heappush(self.maxh, -(minPop)) 
            heapq.heappush(self.minh, -maxPop) 

    def findMedian(self) -> float:
        if (len(self.minh) + len(self.maxh)) % 2 == 1:
            return -(self.maxh[0])
        else:
            return (-(self.maxh[0]) + self.minh[0]) / 2 
        