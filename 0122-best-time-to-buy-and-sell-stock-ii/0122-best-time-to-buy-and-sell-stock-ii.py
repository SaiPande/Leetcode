class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for sell in range(1,len(prices)):
                if prices[sell] > prices[sell-1]:
                    profit += prices[sell]-prices[sell-1]                
        return profit