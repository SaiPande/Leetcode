class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        validsubstringno = 0
        currentsubstring = 1
        previoussubstring = 0

        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                currentsubstring +=1
            else:
                previoussubstring = currentsubstring
                currentsubstring = 1

            if previoussubstring >= currentsubstring:  #if its valid for 000111, it is valid for 01 and 0011
                validsubstringno +=1
        return validsubstringno                
