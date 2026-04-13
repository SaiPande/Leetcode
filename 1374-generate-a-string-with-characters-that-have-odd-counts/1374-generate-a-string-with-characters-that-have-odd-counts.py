class Solution:
    def generateTheString(self, n: int) -> str:
        str = ""
        if n%2 == 0:
            if n == 2:
                return 'ab'
            else:    
                return 'a'*(n-1)+'b'
        else:
            return 'a'*n   