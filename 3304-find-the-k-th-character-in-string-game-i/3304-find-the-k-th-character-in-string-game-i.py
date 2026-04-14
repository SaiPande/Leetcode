class Solution:
    def kthCharacter(self, k: int) -> str:
        word = 'a'
        word2 = ''
        while(len(word) <= k):
            char = ''
            j = 0
            word2 = word
            while(j < len(word)):
                char = chr(ord(word[j])+1)
                j+= 1
                word2 += char
            word = word2
    
        return word[k-1]  

