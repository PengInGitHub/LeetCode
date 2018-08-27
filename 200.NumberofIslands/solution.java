public class Solution {
  public int numIslands(char[][]grid){ 
    int res = 0;
    for (int i = 0; i < grid.length; i++) {
      for (int j = 0; j < grid[0].length; j++) {
        if (grid[i][j] == '1') {
          dfs(grid, i, j);
          res++;
        } 
      }
    }
    return res;
  }

  private void dfs(char[][]grid, int i, int j){
    if(i<0 || j<0 || i>=grid.length || j>=grid[0].length || grid[i][j] == '0')return;
    grid[i][j] = '0';
    dfs(grid, i, j+1);
    dfs(grid, i, j-1);
    dfs(grid, i+1, j);
    dfs(grid, i-1, j);
  }  

    public static void main(String[] args) { 
		Solution mySolution = new Solution();
    
    char[][] grid =  {{'1','1','1','1','0'},
                      {'1','1','0','1','0'},
                      {'1','1','0','0','0'},
                      {'0','0','0','0','1'}};

    if (mySolution.numIslandsUpdate(grid) == 2){
      System.out.println("the func passed the test");
    } 
  } 

  //resource
  //https://laioffer.com/zh/videos/2018-04-11-200-number-of-islands/
  //four directions in a manner of 2D array
  final static int[][] dirs = {{-1,0}, {1,0}, {0,-1}, {0,1}};
  
  public int numIslandsUpdate(char[][] grid){
    //sanity check
    if(grid == null || grid.length == 0 || grid[0].length ==0){
      return 0;
    }
    int rows = grid.length;
    int cols = grid[0].length;
    int count = 0;
    //iterate rows
    for(int i = 0; i < rows; i++){
      //iterate cols
      for(int j = 0; j < cols; j++){
        //found 1
        if(grid[i][j]=='1'){
            count++;
            //from this point, search other 1 vertically or horizontally next to it
            dfsNew(grid, i, j, rows, cols);
        }
      }
    }
    return count;
  }

  private void dfsNew(char[][] grid, int x, int y, int rows, int cols){
    //recrsive func, has base case part and recursion part

    //base case - conditions not to search further
    //two cases 1.go beyond the boundary 2.current coordinate is sea(0) not land(1)
    if(x<0 || x>=rows || y<0 || y>=cols || grid[x][y]=='0'){
      return;
    }

    //recursion
    //this step refers to that grid[x][y] = '1'
    //so firstly set the coordinate value to 0
    grid[x][y] = '0';
    //then traverse on the four directions
    for(int[] dir:dirs){
      //get value of neighbor coordinate
      int neiX = dir[0]+x;
      int neiY = dir[1]+y;
      //traverse
      dfsNew(grid, neiX, neiY, rows, cols);
    }
  } 
}