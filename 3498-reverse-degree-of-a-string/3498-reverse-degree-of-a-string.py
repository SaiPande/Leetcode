class Solution:
    def reverseDegree(self, s: str) -> int:
        sm = 0 
        for i in range(len(s)):
            sm += (97+26-ord(s[i]))*(i+1)
        return sm    