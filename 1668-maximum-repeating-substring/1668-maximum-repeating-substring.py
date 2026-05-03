class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        
        count = 0
        repword = word

        while repword in sequence: 
            count += 1
            repword += word
            print(count)
        return count        
