class Solution {
    public int lengthOfLongestSubstring(String s) {
        if(s.length() == 0) return 0;
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        int max = 0;
        for(int i = 0, j = 0; i < s.length(); ++i){
            /*char already in the map*/
            if(map.containsKey(s.charAt(i))){
                /*move the left pointer to the pos where the repeated char found in the last time
                  i: the right pointer to scan the string
                  j: the left pointer to identify where the new substring starts*/
                j = Math.max(j, map.get(s.charAt(i))+1)  ; 
            }
            /*if char not exists in the map
              add char to the map, update max val*/
            map.put(s.charAt(i),i);
            max = Math.max(max, i-j+1);
        }
        return max;
    }
}