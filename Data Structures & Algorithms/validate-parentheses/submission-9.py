class Solution:
    def isValid(self, s: str) -> bool:
        close = []
        if len(s) < 2:
            return False
        for i in range(len(s)):
            x = s[-1]
            s = s[:-1]
            if x == ")" or x == "}" or x == "]":
                close.append(x)
                if len(s) < 1:
                    return False
            if len(close) < 1:
                return False
            if x == "(":
                if close.pop() != ")":
                    return False
            elif x == "{":
                if close.pop() != "}":
                    return False
            elif x == "[":
                if close.pop() != "]":
                    return False
            
        if len(close) > 0:
            return False
        return True
                    

            
        