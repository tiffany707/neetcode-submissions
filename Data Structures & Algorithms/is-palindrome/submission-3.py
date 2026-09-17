class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = []
        for c in s:
            if c.isalnum():
                res.append(c.lower())
        print(res)
        print(res[::-1])
        return res == res[::-1]