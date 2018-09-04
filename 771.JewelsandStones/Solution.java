//ref
//https://stackoverflow.com/questions/3799130/how-to-iterate-through-a-string
class Solution {
    public int numJewelsInStones(String J, String S) {
        int count = 0;
        for(char j : J.toCharArray()){
            for(char s : S.toCharArray()){
                if(j==s){
                    count++;
                }
            }
        }
        return count;
    }
}