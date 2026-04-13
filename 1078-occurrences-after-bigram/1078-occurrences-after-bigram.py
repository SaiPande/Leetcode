class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        output = []
        words = []
        for i in text.split():
            words.append(i)
        
        for i in range(2, len(words)):
            if words[i-2] == first and words[i-1] == second:     
                output.append(words[i])
    
        return output