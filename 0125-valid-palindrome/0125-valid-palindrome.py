class Solution:
    def isPalindrome(self, s: str) -> bool:
        str1 = ''
        for i in s:
            if i.isalnum():
                str1 += i.lower()

        n = len(str1)
        if n == 1:
            return True

        if n%2 == 0:
            s1 = str1[0:(n//2)]
            s2 = str1[n//2:n][::-1]
            #print(s1 + '   '+ s2+ 'even')
            if s1 == s2:
                return True
            return False
                
        else: 
            s1 = str1[0:(n//2)]
            s2 = str1[(n//2)+1:n][::-1]
            #print(s1 + '   '+ s2+ 'odd')  
            if s1 == s2:
            #    print('in odd iffff')
                return True
            return False



