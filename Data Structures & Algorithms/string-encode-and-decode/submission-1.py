class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for n in strs:
            res += str(len(n)) + "#"
            for c in n:
                res += c
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        num = ""
        word = ""
        ans=[]
        i = 0
        while i < len(s):
            if s[i] == "#":
                num = int(num)
                i += 1
                ans.append(s[i:i+num])
                i += num
                num = ""
            elif s[i] in "0123456789":
                num += s[i]
                i += 1
        return ans
