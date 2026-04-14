class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        
        onecount = s.count('1')
        zerocount = len(s) - onecount
        
        return (onecount-1)*'1'+zerocount*'0'+'1'
