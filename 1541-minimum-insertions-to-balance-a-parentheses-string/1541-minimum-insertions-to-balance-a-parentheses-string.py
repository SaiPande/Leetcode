class Solution:
    def minInsertions(self, s: str) -> int:
        
        stk = []
        minbal = 0
        i = 0
        while i < len(s):
            if s[i] == '(':
                stk.append(s[i])
            else:
                if i + 1 < len(s) and s[i + 1] == ')':
                    i += 1  
                else:
                    minbal += 1  
                
                if stk:
                    stk.pop()  
                else:
                    minbal += 1      
            i+=1         
        
        if stk:
            for i in stk:
                if i == '(':
                    minbal+=2
                else:
                    minbal+=1
        return minbal        

