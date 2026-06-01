class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        if len(cost)<2:
            return cost[0]
        elif len(cost)<3:
            return cost[0]+cost[1]   
        count = 0
        i = 2
        while i < len(cost):
            if cost[i] <= cost[i-1] and cost[i] <= cost[i-2]:
                count += cost[i-1]+cost[i-2]
            else:
                count+=cost[i]   
            i=i+3   

        leftover_start = i - 2
        while leftover_start < len(cost):
            count += cost[leftover_start]
            leftover_start += 1     
        return count        
                    