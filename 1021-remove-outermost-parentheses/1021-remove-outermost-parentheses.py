class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stk = []
        output = []
        start = 0
        for i in range(len(s)):
            if s[i] == '(':
                stk.append('(')
            else:
                if stk:
                    stk.pop()
                    if not stk:
                        output.append(s[start+1:i])
                        start = i+1
        return ''.join(output)                                