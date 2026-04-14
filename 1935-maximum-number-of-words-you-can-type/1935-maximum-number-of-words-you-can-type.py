class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        lst = text.split(' ')
        count = 0
        flag = 0
        for i in lst:
            j = 0
            while(j < len(i)):
                if i[j] in brokenLetters:
                    flag = 1
                    break
                else:
                    j+=1    
            if flag == 0:        
                count += 1      
            flag = 0      
                

        return count        