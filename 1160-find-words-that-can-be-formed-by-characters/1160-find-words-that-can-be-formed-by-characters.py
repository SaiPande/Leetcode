from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        freq = Counter(chars)
        count = 0
        for i in range(len(words)):
            validstring = True
            tempmap = Counter(words[i])
            for ch in tempmap:
                if tempmap[ch] > freq[ch]:
                    validstring = False
                    break 
            if validstring == True:
                count += len(words[i])
        return count