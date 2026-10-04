class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        n = len(points)
        maxarea = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    maxarea = max(maxarea, 0.5*abs(points[i][0]*(points[j][1] - points[k][1]) + points[j][0]*(points[k][1] - points[i][1]) + points[k][0]*(points[i][1] - points[j][1])))
        return maxarea            