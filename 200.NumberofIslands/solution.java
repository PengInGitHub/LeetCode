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
     	char [][]grid = new char [3][3];
		grid[0][0] = '1';
		grid[0][1] = '1';
		grid[0][2] = '1';
		grid[1][0] = '0';
		grid[1][1] = '1';
		grid[1][2] = '1';
		grid[2][0] = '1';
		grid[2][1] = '1';
		grid[2][2] = '0';        
     
		System.out.print(mySolution.getIslandNum(grid));
	} 
      
}