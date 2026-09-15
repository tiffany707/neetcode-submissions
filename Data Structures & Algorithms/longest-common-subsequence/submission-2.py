class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        lookup = {}

        def rec(i, j):
            if (i,j) in lookup:
                return lookup[(i,j)]
            if j >= len(text2) or i >= len(text1):
                return 0
            
            if text1[i] == text2[j]:
                res = 1 + rec(i + 1, j + 1)
            else:
                res = max(rec(i, j + 1), rec(i + 1, j))
            lookup[(i,j)] = res
            return res

        return rec(0,0)