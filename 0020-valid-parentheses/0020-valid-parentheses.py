class Solution:
    def isValid(self, s: str) -> bool:
        freq = {')':'(', ']':'[','}':'{'}
        stack = []
        for i in s:
            if i in freq:
                if not stack or stack.pop() != freq[i]:
                    return False
            else:
                stack.append(i)         
 
        return not stack