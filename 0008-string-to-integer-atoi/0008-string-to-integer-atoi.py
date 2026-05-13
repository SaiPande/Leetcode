class Solution:
    def myAtoi(self, s: str) -> int:
        #atoi -> ASCII to Integer
        if s == '':
            return 0
        opt = ''
        i = 0
        sign = 1
        if s[0].isalpha():
            return 0

        while i < len(s) and s[i] == ' ':
            i+=1    
        if i<len(s) and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i+=1    
        for j in range(i,len(s)):
            if s[j].isdigit():
                opt += s[j]
            else:
                break
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if not opt:
            return 0
        if sign*int(opt)>INT_MAX:
            return INT_MAX
        elif sign*int(opt)<INT_MIN:
            return INT_MIN
        else:
            return sign*int(opt)      
