class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        lookup = {
            "*": lambda a, b: a * b,
            "/": lambda a, b: math.trunc(b / a), 
            "+": lambda a, b: a + b,
            "-": lambda a, b: b - a}
        
        for i in range(len(tokens)):
            if tokens[i] in lookup:
                a = stack.pop()
                b = stack.pop()
                ans = lookup[tokens[i]](int(a), int(b))
                print(ans)
                stack.append(ans)
            else:
                stack.append(tokens[i])
        return int(stack[0])


        