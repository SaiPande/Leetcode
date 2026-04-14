class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        '''ifcount = 0
        if n <= 0:
            return False
        el n == 1:
            return True
        else:
            if(n%2 == 0):
                count+=1
                return self.isPowerOfTwo(n//2)
            else:
                return False     
        return True  '''             

        return n > 0 and (n & (n-1)) == 0