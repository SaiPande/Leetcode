class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        

        if p == '.*':
            return True
        stack = [] 
        i = 0
        j = 0
        while i < len(p) or stack:    
            if i == len(p):
                if j == len(s):
                    return True
                i, j = stack.pop()
                continue  
            if i < len(p)-1 and p[i+1] == '*':
                prev = p[i]
                if j < len(s) and (s[j] == prev or prev == '.'):
                    stack.append((i, j + 1)) 
                i += 2   
            elif i< len(p) and p[i] == '.':
                i+=1
                j+=1
            elif j < len(s) and i<len(p) and p[i] == s[j]:
                i+=1
                j+=1
            else:
                if stack:
                    i, j = stack.pop()
                else:
                    return False   
        if i == len(p) and j == len(s):
            return True
        return False                 

