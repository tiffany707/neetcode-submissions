class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needLookup = collections.defaultdict(int)
        haveLookup = collections.defaultdict(int)
        for i in range(len(t)):
            needLookup[t[i]] += 1
        need = len(needLookup)
        have = 0
        l = 0
        ans = [0, float('inf')]

        for r in range(len(s)):
            haveLookup[s[r]] += 1
            if haveLookup[s[r]] == needLookup[s[r]]:
                have += 1
                while have == need:
                    if r - l + 1 < ans[1] - ans[0] + 1:
                        ans = [l, r]
                    haveLookup[s[l]] -= 1
                    if haveLookup[s[l]] < needLookup[s[l]]:
                        have -= 1
                    l += 1
        if ans[1] == float('inf'):
            return ""
        return s[ans[0]: ans[1] + 1]
