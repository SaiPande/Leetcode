from collections import Counter 

class Solution:
    def maxScore(self, s: str) -> int:
        count = Counter(s)
        score = 0
        for i in range(0, len(s)-1):
            st1 = s[0:i+1]
            count0 = 0
            count1 = 0
            for j in st1:
                if j == '0':
                    count0 += 1
                else: 
                    count1 +=1    
            ones = count['1'] - count1  
            if (count0 + ones > score):
                score = count0 + ones 
        return score        