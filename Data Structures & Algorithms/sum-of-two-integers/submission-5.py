class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b:
            mask = 0xFFFFFFFF 
            temp = ((a & b) << 1) & mask
            a = (a ^ b) & mask 
            b = temp

        return a if a <= 0x7FFFFFFF else ~(a^mask)