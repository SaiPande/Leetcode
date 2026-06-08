class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        substr = {}
        substr1 = []
        primelist = []
        for i in range(len(s)):
            for j in range(i,len(s)):
                substr1.append(int(s[i:j+1]))
        substr = list(set(substr1)) 
        for i in substr:
            if i == 0 or i == 1:
                continue    
            isprime = self.primenum(i)
            if isprime:
                primelist.append(i)

        max3 = sorted(primelist, reverse=True)[:3]
        return sum(max3)        

    def primenum(self,n)->Boolean:
        if n <= 1: return False   
        if n <= 3: return True   
        if n % 2 == 0 or n % 3 == 0: return False 
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
            
        return True