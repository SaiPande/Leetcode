class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        resultstr = []
        for i in words:
            count = 0
            for j in range(len(i)):
                count += weights[ord(i[j]) - ord('a')]
            val = count % 26
            resultstr.append(chr(ord('z') - val))   
        return ''.join(resultstr)        