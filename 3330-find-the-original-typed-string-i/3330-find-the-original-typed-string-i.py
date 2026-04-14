class Solution:
    def possibleStringCount(self, word: str) -> int:
        total = 0
        count = 0
        for i in range(0,len(word)-1):
            if word[i] == word[i+1]:
                count += 1
            else:
                total += count  
                count = 0
        total += count       
        
        return total + 1           


         
        
   