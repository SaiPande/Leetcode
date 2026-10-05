class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = []
        score = 0
        deep = 0
        for i in s:
            if i == '(':
                stk.append('(')
                deep = len(stk)
            else:
                if stk:
                    stk.pop()
                    if deep == len(stk) + 1:
                        score += 2 ** len(stk)
                        deep = 0 

        return score

