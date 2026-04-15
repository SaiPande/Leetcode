class Solution:
    def makeFancyString(self, s: str) -> str:
        str1 = ''
        count = 0
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                count += 1
                if count >= 2:
                    continue
                else:                        
                    str1 += s[i]

            else:
                count = 0
                str1 += s[i]

        
        str1 += s[len(s)-1]               

        return str1                   