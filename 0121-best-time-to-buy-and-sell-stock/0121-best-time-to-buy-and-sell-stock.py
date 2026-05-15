class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        sell = 1
        minbuydate = prices[0]
        profit = 0
        while sell<len(prices):

            if prices[sell] < minbuydate:
                minbuydate = prices[sell]

            elif prices[sell]>minbuydate:
                if profit< prices[sell]-minbuydate:        
                    profit = prices[sell]-minbuydate
            
            sell+=1   

        return profit