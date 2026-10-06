class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        stk = []
        cntclose = 0
        for i in s:
            if i == '(':
                stk.append('(')
            else:
                if stk:
                    stk.pop()
                else:
                    cntclose += 1        

        return len(stk)+cntclose                