import heapq
import math

class Solution:
    def minimumCost(self, n: int, highways: list[list[int]], discounts: int) -> int:
        adjlist = [[] for _ in range(n)]
        
        for start, dest, cost in highways:    
            adjlist[start].append((dest,cost))
            adjlist[dest].append((start,cost))

        print(adjlist)
      
        minheap = [(0,0,0)]
        discnt = [[math.inf]*(discounts+1) for _ in range(n)]
        discnt[0][0] = 0

        visited = [[False]*(discounts+1) for _ in range(n)]

        while minheap:
            currentcost, currentnode, discountused = heapq.heappop(minheap)

            if visited[currentnode][discountused]:
                continue
            visited[currentnode][discountused] = True    


            for neighbor, weight in adjlist[currentnode]:
                newcost = currentcost + weight
                if newcost < discnt[neighbor][discountused]:
                    discnt[neighbor][discountused] = newcost
                    heapq.heappush(minheap, (newcost, neighbor, discountused))

                if discountused < discounts:
                    newcostwithdiscount = currentcost + weight//2
                    if newcostwithdiscount < discnt[neighbor][discountused + 1]:
                        discnt[neighbor][discountused + 1] = newcostwithdiscount
                        heapq.heappush(minheap, (newcostwithdiscount, neighbor, discountused+1))   

        mincost = min(discnt[n-1])
        return -1 if mincost == float("inf") else mincost        



        


        
        