class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            s = str(len(s)) + "#" + s
            res += s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        num = ""
        while i < len(s):
            if s[i] == "#":
                i += 1
                num = int(num)
                ans.append(s[i:i+num])
                i = i + num
                num = ""
            else:
                num += s[i]
                i += 1
        return ans


