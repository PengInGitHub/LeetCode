class Solution {
    public int hammingDistance(int x, int y) {
        int count = 0;
        for(int i=0; i<31; i++){
            int bin_x = x%2;
            int bin_y = y%2;
            if(bin_x !=bin_y){
                count++;
            }
            x>>=1;
            y>>=1;
        }
        return count;
    }
}