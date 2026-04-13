class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        Output = []
        for i,s in enumerate(words): 
            if (s.__contains__(x)):
                Output.append(i)
        return Output       