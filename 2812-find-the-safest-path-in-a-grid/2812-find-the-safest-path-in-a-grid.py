class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()
        min_dist = {}

        def validneighbor(r,c):
            return max(r,c) < n and min(r,c)>=0

        def bfstofindistance():
            for r in range(n):   ## finding thiefs and putting them in a queue
                for c in range(n):  
                    if grid[r][c]:
                        q.append([r,c,0])     # (append row, col and distance from thief) here distance from thief == 0
                        min_dist[(r,c)] = 0

            while q:    ## BFS from each thief to find the distach of each cell from a thief
                r, c, dist = q.popleft()     
                nei = [[r+1,c], [r,c+1], [r-1,c], [r,c-1]]  

                for r2,c2 in nei:  
                    if validneighbor(r2,c2) and (r2,c2) not in min_dist:
                        q.append([r2,c2,dist+1])     
                        min_dist[(r2,c2)] = dist+1
            return min_dist

        min_dist = bfstofindistance()

        maxHeap = [(-min_dist[(0,0)], 0, 0)] #distance, row, col    ##python doesnt support maxheap so we negate the number
        visited = set()   # avoid duplicate checks 

        visited.add((0,0))

        while maxHeap:   # distrija   (greedy)
            dist, r3,c3 = heapq.heappop(maxHeap)  
            dist = -dist
            if (r3,c3) == (n-1,n-1):
                return dist
            nei = [[r3+1,c3], [r3,c3+1], [r3-1,c3], [r3,c3-1]]   

            for r4,c4 in nei:  
                if validneighbor(r4,c4) and (r4,c4) not in visited:
                    visited.add((r4,c4))
                    dist2 = min(dist, min_dist[(r4, c4)])
                    heapq.heappush(maxHeap, (-dist2, r4,c4))     
                    
            


