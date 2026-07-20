class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])


        for _ in range(k):

            temp_grid = [[0]*cols for _ in range(rows)]

            for row in range(rows):
                for col in range(cols-1):
                    temp_grid[row][col+1] = grid[row][col]

            for row in range(rows-1):
                temp_grid[row+1][0] = grid[row][cols-1]

            temp_grid[0][0] = grid[rows-1][cols-1]

            grid = temp_grid

        return grid                
                