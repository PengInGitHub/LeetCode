class Solution {
    public String countAndSay(int n) {
        /*use recursion*/
        if (n == 1) return "1";
        char[] res = countAndSay(n - 1).toCharArray();
        int count = 0;
        char cur = res[0];
        StringBuilder sb = new StringBuilder();
        
        for(int i = 0; i < res.length; i++){
            if (cur != res[i]){
                sb.append(count);
                sb.append(cur);
                /*update cur and count*/
                cur = res[i];
                count = 1;
            }else{
                count++;
            }
        }
        sb.append(count > 0 ? count + String.valueOf(cur) : "");
        return sb.toString();
    }  
}