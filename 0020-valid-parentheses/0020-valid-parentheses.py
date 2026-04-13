class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) < 2:
            return False
        for i in s:
            if i == "(" or i == '[' or i == '{':
                stack.append(i)
            if len(stack) >= 1:
                if i == ")" and stack[-1] == "(":
                    stack.pop()
                elif i == "}"  and stack[-1] == "{":
                    stack.pop()
                elif i == "]"  and stack[-1] == "[":
                    stack.pop()
                elif i == ")" and stack[-1] != "(":
                    stack.append(i)
                elif i == "}" and stack[-1] != "{":
                    stack.append(i) 
                elif i == "]" and stack[-1] != "[":
                    stack.append(i)    
            else:
                stack.append(i)         
 
        print(stack)   
        if len(stack) == 0:
            return True
        else:
            return False    

