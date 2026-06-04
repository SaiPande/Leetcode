class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        wave = 0
        start = num1
        end = num2+1
        if num2< 101:
            return 0     

        for i in range(start, end):
            s = str(i)
            for j in range(1,len(s)-1):
                if (s[j-1] > s[j] and s[j+1] > s[j]) or (s[j-1] < s[j] and s[j+1] < s[j]):
                    wave+=1
        return wave            



