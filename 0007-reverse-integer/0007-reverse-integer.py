class Solution:
    def reverse(self, x: int) -> int:

        if x == 0:
            return 0

        stack = []
        isneg = -1 if x < 0 else 1
        x1 = abs(x)
        
        while x1>0:
            stack.append(str(x1%10))
            x1//=10
        reversednum = int(''.join(stack))       
        if isneg*reversednum <= -2**31 or isneg*reversednum >= (2**31-1):
            return 0
        return isneg*reversednum 