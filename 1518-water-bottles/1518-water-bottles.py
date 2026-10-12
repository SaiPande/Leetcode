class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        t1 = numBottles
        qu = 0

        while numBottles >= numExchange:
            qu += numExchange
            numBottles-=numExchange
            
            numBottles+=1

        return qu+numBottles


