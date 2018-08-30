package Solution

func numIslands(grid [][]byte) int {
    if grid == nil || len(grid) == 0{
        return 0
    }
    
    rows := len(grid)
    cols := len(grid[0])
    count := 0
    
    for i:=0; i<rows; i++{
        for j:=0; j<cols; j++{
            if grid[i][j] == '1'{
                dfs(grid, i, j, rows, cols)
                count++
            }
        }
    }
    return count
}

func dfs(grid [][]byte, x, y, rows, cols int){
    if x<0 || y<0 || x>=rows || y>=cols || grid[x][y]=='0'{
        return
    } 
    grid[x][y]='0'
    
    dirs := [][]int{{-1,0}, {1,0}, {0,-1}, {0,1}}
    for _, dir := range dirs{
        neiX := dir[0]+x
        neiY := dir[1]+y
        dfs(grid, neiX, neiY, rows, cols)
    }
    
}