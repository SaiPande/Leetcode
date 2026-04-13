class Solution:
    def romanToInt(self, s: str) -> int:
        num_count = 0
        i = 0
        while(i < len(s)):
            if i < len(s)-1 and s[i] == 'I' and s[i+1] == 'V':
                num_count = num_count + 4
                i+=2
            elif i < len(s)-1 and s[i] == 'I' and s[i+1] == 'X':
                num_count = num_count + 9
                i+=2
            elif i < len(s)-1 and s[i] == 'X' and s[i+1] == 'L':
                num_count = num_count + 40
                i+=2
            elif i < len(s)-1 and s[i] == 'X' and s[i+1] == 'C':
                num_count = num_count + 90
                i+=2
            elif i < len(s)-1 and s[i] == 'C' and s[i+1] == 'D':
                num_count = num_count + 400
                i+=2
            elif i < len(s)-1 and s[i] == 'C' and s[i+1] == 'M':
                num_count = num_count + 900
                i+=2                     
            elif s[i] == 'I':
                num_count += 1
                i+=1
            elif s[i] == 'V':
                num_count += 5
                i+=1
            elif s[i] == 'X':
                num_count += 10
                i+=1
            elif s[i] == 'L':
                num_count += 50
                i+=1
            elif s[i] == 'C':
                num_count += 100
                i+=1
            elif s[i] == 'D':
                num_count += 500
                i+=1
            elif s[i] == 'M':
                num_count += 1000
                i+=1    
            #print(num_count)
        return num_count        

