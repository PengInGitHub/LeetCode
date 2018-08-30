class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid == None or len(grid) == 0:
            return 0

        #length of row and col
        rows = len(grid)
        cols = len(grid[0])

        #init a counter, increase by 1 if a continent is found
        count = 0
        #loop through the grid x and y-axis
        #x-rows
            #deepth first searching
        def dfs(grid, x, y, rows, cols):
            #define the move directions of a dot
            #use a 2D array
            #left, right, up, down
            dirs = [[-1,0], [1,0], [0,-1], [0,1]]

            #situations to stop (return)
            #boundry: 1.x or y is neg,
                     #2.x or y is larger than num of row or num of col
                     #3.dot is a zero (sea) instead of one (continent)
            if x<0 or y<0 or x>=rows or y>=cols or grid[x][y] == '0':
                return
            #not return, means this dot has value of '1'
            #firstly update the value to '0', indicates that this dot is not necessary to be considered any more
            grid[x][y] = '0'
            #mistake made here: grid[x][y] == '0'
            
            #move the dot
            #has four directions to move, so iterate them
            for dir in dirs:
                neighborX = x+dir[0] #dir[0] means x value only
                neighborY = y+dir[1] #dir[1] means y value only
                dfs(grid,neighborX, neighborY, rows, cols)
        for i in range(0, rows):
            #y-cols
            for j in range(0, cols):
                #if a continent is found
                if grid[i][j] == '1':
                    #search its neighbor if it is also a continent
                    dfs(grid, i, j, rows, cols)
                    count += 1

        #return the count
        return count
    

        
        
        
    
        
