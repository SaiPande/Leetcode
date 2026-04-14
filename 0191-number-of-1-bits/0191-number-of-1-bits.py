class Solution:
    def hammingWeight(self, n: int) -> int:
        
        dec = bin(n)[2:]
        count = 0
        for i in dec:
            if i == '1':
                count += 1
        return count         