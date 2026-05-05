class Solution:
    def isHappy(self, n: int) -> bool:
        set1 = set()
        if n == 1:
            return True
        while n!= 1 and n not in set1: 
            set1.add(n)
            sum = 0
            while (n>0):
                t = n%10
                sum += t*t
                n = n//10  
            n = sum
            if n in set1:
                return False
            if sum == 1:
                return True
        