class MinStack:

    def __init__(self):
        self.arr = []
        self.minArr = []

    def push(self, val: int) -> None:
        print(val)
        self.arr.append(val)
        if len(self.arr) > 1 and val < self.minArr[len(self.minArr)-2]:
            minVal = val
        elif len(self.minArr) > 1:
            minVal = self.minArr[len(self.minArr)-2]
        else:
            minVal = val
        self.minArr.append(minVal)
        self.minArr.append(val)

    def pop(self) -> None:
        self.arr = self.arr[:len(self.arr)-1]
        self.minArr = self.minArr[:len(self.minArr)-2]
 

    def top(self) -> int:
        return self.arr[len(self.arr)-1]

    def getMin(self) -> int:
        return self.minArr[len(self.minArr)-2]
        
