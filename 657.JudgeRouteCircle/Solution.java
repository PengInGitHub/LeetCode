class Solution {
    public boolean judgeCircle(String moves) {
        if(moves.length()%2 != 0)return false;
        int x = 0;
        int y = 0;
        for (char move : moves.toCharArray()){
            if(move=='U') y -= 1;
            else if(move=='D') y += 1;
            else if(move=='L') x -= 1;
            else x += 1;
        }
        if(x==0 && y==0)return true;
        return false;
    }
}