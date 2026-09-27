class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        output = []

        for i in range(len(s)):
            if s[i] == ')':
                lst = []
                while stack and stack[-1] != '(':
                    t = stack.pop()
                    lst.append(t[::-1])     
                if stack:
                    stack.pop() 
                stack.append(''.join(lst))
            else:
                stack.append(s[i])    
        return ''.join(stack)       
