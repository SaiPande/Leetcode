class Solution:
    def greatestLetter(self, s: str) -> str:

        setalpha = set(s)

        for i in range(25,-1,-1):
            upper = chr(ord('A')+i)
            lower = chr(ord('a')+i)

            if upper in setalpha and lower in setalpha:
                return upper

        return ""        
                
                    
