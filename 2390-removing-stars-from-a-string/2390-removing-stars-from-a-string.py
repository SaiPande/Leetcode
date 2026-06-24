class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] == '*':
                if stack:
                    stack.pop()        
            else:
                stack.append(s[i])
        if len(s) > 0:
            return ''.join(stack)   
        return ''             
