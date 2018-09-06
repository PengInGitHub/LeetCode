class Solution {
    public void rotate(int[][] matrix) {
        //modify in place
        //two steps: first rotation matrix[i][j] = matrix[j][i]
        //then swap matrix[i][j] = [i][n-1-j] when j<n/2 
        //e.g. in case there are n=4 cols, swap col[0] with col[3], swap col[1] with col[2]
        
        int n = matrix.length;

        //step 1, rotate matrix
        //i is index of x, while j is of y
        for(int i=0; i<n; i++){
            //for(int j=0; j<i; j++){
            //alternative
            for(int j=i; j<n; j++){
                //rotate
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = tmp;
            }
        }
        //step 2, swap cols
        for(int i=0; i<n; i++){
            for(int j=0; j<(n/2); j++){
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[i][n-1-j];  
                matrix[i][n-1-j]  = tmp; 
            }
        }        
    }
}