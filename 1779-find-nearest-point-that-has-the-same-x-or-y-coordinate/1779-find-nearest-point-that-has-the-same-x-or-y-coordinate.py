class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        if len(points) == 1:
            if points[0][0] == x or points[0][1] == y:
                return 0
            return -1    
        min = 999999999
        idx = -1
        for i in range(len(points)):
            if x == points[i][0] or y == points[i][1]:
                mdist = abs(points[i][0]-x) + abs(points[i][1]-y)
                if mdist < min:
                    min = mdist
                    idx = i
        return idx            
