class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        if not costs:
            return 0
        if costs[0]>coins:
            return 0    
        costs.sort()
        no_of_icecream = 0
        for i in range(len(costs)):
            if costs[i] <= coins:
                no_of_icecream+=1
                coins-=costs[i]
            else:
                break    
        return no_of_icecream   
