class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            indexofchar = word.index(ch)
            strr = word[0:indexofchar+1]
            return strr[::-1] + word[indexofchar+1:len(word)]

        else: 
            return word    