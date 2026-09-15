class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)

        for i in range(len(ans)):
            count = 0
            curr = i
            while i:
                i = i & (i-1)
                count += 1
            ans[curr] = count

        return ans