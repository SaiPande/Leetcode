class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_str = str(x)
        j = len(num_str) - 1
        i = 0
        while(i < j):
            if num_str[i] == num_str[j]:
                j-= 1
                i+= 1
            else: 
                return False
        
        return True