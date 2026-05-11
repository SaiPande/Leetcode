class Solution:
    def reverseVowels(self, s: str) -> str:
        
        i = 0
        j = len(s) -1
        slist = list(s)
        while i<j:    

            if slist[i] not in 'aeiouAEIOU':
                i+= 1
            if slist[j] not in 'aeiouAEIOU':
                j-=1
            if slist[i] in 'aeiouAEIOU' and slist[j] in 'aeiouAEIOU':
                slist[i], slist[j] = slist[j], slist[i] 
                i+=1
                j-=1
        return ''.join(slist)           
                