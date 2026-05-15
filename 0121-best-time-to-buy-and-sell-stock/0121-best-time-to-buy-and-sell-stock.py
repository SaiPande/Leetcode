class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell = 1
        minbuydate = prices[0]
        profit = 0
        for sell in range(len(prices)):

            if prices[sell] < minbuydate:
                minbuydate = prices[sell]

            elif prices[sell]>minbuydate:
                pro= prices[sell]-minbuydate
                if profit< pro:        
                    profit = pro
        return profit