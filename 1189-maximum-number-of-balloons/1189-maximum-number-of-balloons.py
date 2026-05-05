class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = {}

        for i in text:
            freq[i] = freq.get(i,0)+1
        count = 0
        b = freq.get('b', 0)
        a = freq.get('a', 0)
        l = freq.get('l', 0)
        o = freq.get('o', 0)
        n = freq.get('n', 0)

        while b>0 and a>0 and l>1 and o>1 and n>0:
            b -= 1
            a -= 1
            l -= 2
            o -= 2
            n -= 1
            count += 1

        return count    
