class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        targetletter = ord(target)
        minimum = 99999
        minmaxletter = ''
        for i in range(len(letters)):
            if ord(letters[i]) > targetletter and  ord(letters[i]) < minimum:
                minimum = ord(letters[i])
                minmaxletter = letters[i]
        if minmaxletter != '':
            return minmaxletter
        else:
            return letters[0]           