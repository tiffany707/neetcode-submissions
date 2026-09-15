class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        lookup = {}

        def rec(w):
            if w in lookup:
                return lookup[w]
            if s[0:len(w)] != w:
                return False
            if s == w:
                return True
            for n in wordDict:
                if s[len(w):len(w)+len(n)] == n:
                    if rec(w + n):
                        return True
            lookup[w] = False
            return False

        for n in wordDict:
            if rec(n):
                return True
        return False