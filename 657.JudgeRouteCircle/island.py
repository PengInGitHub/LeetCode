# Hello World program in Python
import numpy

class IslandSun:
    def findIsland(self, grid):
        if grid == None or len(grid) == 0:
            return 0
        #length of row and col
        rows = len(grid)
        cols = len(grid[0])

        #init a counter, increase by 1 if a continent is found
        count = 0


        def dfs(grid, x, y, rows, cols):
            #define the move directions of a dot
            #use a 2D array
            #left, right, up, down
            dirs = [[-1,0], [1,0], [0,-1], [0,1]]

            #situations to stop (return)
            #boundry: 1.x or y is neg,
                     #2.x or y is larger than num of row or num of col
                     #3.dot is a zero (sea) instead of one (continent)
            if x<0 or y<0 or x>=rows or y>=cols or grid[x][y] == 0:
                return
            #now update 
            grid[x][y] = 0 #mistake here grid[i][j] == 0
            #let it move
            for dir in dirs:
                neighborX = x+dir[0] #dir[0] means x value only
                neighborY = y+dir[1] #dir[1] means y value only
                dfs(grid,neighborX, neighborY, rows, cols)

        k_map = {}
        #iterate x of grid
        for i in range(0, rows):
            #y-cols
            for j in range(0, cols):
                #if a continent is found
                for k in range(0, 5):                      
                    if grid[i][j] == k:
                        #search its neighbor if it is also a continent
                        dfs(grid, i, j, rows, cols)
                        count += 1
                        k_map[k] = count
        #return the count
        return k_map    



matrix = [['0', '1', '0'], ['0', '1', '0'], ['1', '0', '0']]
matrix = [[0,2,1], [0,2,2], [3,4,1]]
solution = IslandSun()
print(matrix)
print solution.findIsland(matrix)