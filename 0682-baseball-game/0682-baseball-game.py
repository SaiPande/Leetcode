class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == '+':
                if len(stack)>=2:
                    score1 = stack[-1]
                    score2 = stack[-2]
                    stack.append(score1+score2)
            elif op == 'D':
                if stack:
                    stack.append(stack[-1]*2)
            elif op == 'C':
                if stack:
                    stack.pop()
            else:
                stack.append(int(op))                
        if len(stack)>0:
            return sum(stack)
        return 0