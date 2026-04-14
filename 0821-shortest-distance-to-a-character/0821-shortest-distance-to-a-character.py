class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        output = []
        final = []
        for i in range(len(s)):
            if s[i] == c:
                output.append(i)
        print(output)
        for i in range(0,len(s)):
            short = 10**9
            for j in output:
                if abs(i-j) < short:
                    short = abs(i-j)
            final.append(short)        
                    

        print(final)
        return final            
