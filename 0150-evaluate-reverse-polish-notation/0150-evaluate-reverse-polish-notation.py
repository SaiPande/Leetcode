class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        result = 0
        ops = {
            "+": lambda a,b: a+b,
            "-": lambda a,b: a-b,
            "*": lambda a,b: a*b,
            "/": lambda a,b: a/b
        }

        for i in tokens:
            if i in '+-*/':
                a = stack.pop()
                b = stack.pop()  
                result = ops[i](b,a)
                stack.append(int(result))

            else:
                stack.append(int(i))
        return int(result)