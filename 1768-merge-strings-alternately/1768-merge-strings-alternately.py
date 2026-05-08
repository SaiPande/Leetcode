class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        l = len(word1) if len(word1)<len(word2) else len(word2)
        mergestr = ""
        for i in range(l):
            mergestr += word1[i] + word2[i]

        if len(word1)>l:
            mergestr += word1[i+1:]
        else:
            mergestr += word2[i+1:]
        return mergestr        
