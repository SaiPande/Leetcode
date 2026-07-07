class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n ==0 :
            return 0

        s = str(n)
        ls = []
        sm = 0
        for i in s:
            if i != '0':
                ls.append(i)
                sm+=int(i)
        return int(''.join(ls))*sm        