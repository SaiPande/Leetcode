class Solution:
    def reverseDegree(self, s: str) -> int:
        count = 0
        for i in range(0,len(s)):
            count += (i+1)*(123-ord(s[i]))

        return count    