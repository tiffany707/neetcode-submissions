class Solution:
    def longestPalindrome(self, s: str) -> str:

        
        ans = [0, 0]

        def rec(l, r):
            nonlocal ans
            while l >= 0 and r < len(s) and s[l] == s[r]:
                    l -= 1
                    r += 1
            print(l, r)
            if (r - 1) - (l + 1) > ans[1] - ans[0]:
                        ans = [l + 1, r -1]
                        print(ans)

        for x in range(len(s)):
            rec(x, x)
            # even
            rec(x, x + 1)
        print(ans)
        return s[ans[0]: ans[1] + 1]


