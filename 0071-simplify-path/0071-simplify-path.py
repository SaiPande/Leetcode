class Solution:
    def simplifyPath(self, path: str) -> str:
        i = 0
        stk = []
        while i < len(path):
            if path[i] == '/':
                i+=1
                temp = ''
                while i< len(path) and path[i] != '/':
                    temp += path[i]
                    i+=1
                if temp != '':
                    stk.append(temp)    
            else:
                i+=1        
        #print(stk)  
        s = stk[::-1]
        #print(s)
        ls = []
        while s:
            if s[-1] == "..":
                s.pop()
                if ls:
                    ls.pop()
            elif s[-1] == '.':
                s.pop()        
            else:
                ls.append(s.pop())
        
        return '/'+'/'.join(ls)

