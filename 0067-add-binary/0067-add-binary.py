class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        sum1 = int(a, 2)+int(b, 2)

        return bin(sum1)[2:]
            