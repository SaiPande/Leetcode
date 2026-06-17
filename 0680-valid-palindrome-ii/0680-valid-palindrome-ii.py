class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        l = 0
        r = len(s) -1

        while l<r:

            if s[l] != s[r]:
                lskip = s[l+1:r+1]
                rskip = s[l:r]
                return lskip == lskip[::-1] or rskip == rskip[::-1]

            l+=1
            r-=1
        return True    