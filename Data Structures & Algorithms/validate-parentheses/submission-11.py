class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {"(":")", "{":"}", "[":"]"}
        stack = []

        for p in s:
            if p in lookup:
                stack.append(p)
            else:
                if not stack:
                    return False
                n = stack.pop()
                if p != lookup[n]:
                    return False
        if stack:
            return False
        return True


