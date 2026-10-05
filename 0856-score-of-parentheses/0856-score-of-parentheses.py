class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = [0]
        score = 0
        deep = 0
        for i in s:
            if i == '(':
                stk.append(0)
                deep = 1
            else:
                top = stk.pop()
                stk[-1] += max(2*top,1)

        return stk.pop()

