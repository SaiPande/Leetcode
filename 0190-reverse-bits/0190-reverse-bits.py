class Solution:
    def reverseBits(self, n: int) -> int:
        stri = bin(n)[2:].zfill(32)
        str2 = ''.join(stri[::-1])
        return int(str2,2)    