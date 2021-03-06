class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    perimeter += 4
                    if x > 0 and grid[y][x-1] == 1: perimeter -= 2
                    if y > 0 and grid[y-1][x] == 1: perimeter -= 2
        return perimeter
                
                    
        