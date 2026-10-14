import math

class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        
        if sum > 9*num:
            return ""
        q, r = divmod(sum, 9)
        ans = "9"*q

        if r>0:
            ans += str(r)
        ans += "0"*(num - len(ans))
        return ans        
        
        
        # lowerrange = (10**(num-1))
        # higherrange = (10**(num))
        # maxval = 0
        # maxnum = 0
        # for i in range(lowerrange, higherrange):
        #     str_i = str(i)
        #     if math.fsum(int(char) for char in str_i) == sum:
        #         sm = math.fsum(int(char)**2 for char in str_i)
        #         if maxval <= sm:
        #             maxval = sm
        #             maxnum = i
                    
        # return str(maxnum) if maxnum >0 else ''         