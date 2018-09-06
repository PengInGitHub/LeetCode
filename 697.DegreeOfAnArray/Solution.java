

class Solution {
    public int findShortestSubArray(int[] nums) {
        Map<Integer, Integer> counts = new HashMap<>();
        Map<Integer, Integer> starts = new HashMap<>();
        Map<Integer, Integer> ends = new HashMap<>();
        int max_count = Integer.MIN_VALUE; 
        int res = Integer.MAX_VALUE; 
        
        //iterate nums, get degree of array
        for(int idx=0; idx<nums.length;idx++){
            int num = nums[idx];
            //not in starts
            if(!starts.containsKey(num)){
                starts.put(num, idx);
                counts.put(num, 0);
            }
            //does exist already
            counts.put(num, counts.get(num)+1);
            ends.put(num, idx);
            //update max_count
            max_count = Math.max(max_count, counts.get(num) );
        }
        
        //iterate counts map, get the minmum subsets contain all numbers of array degree
        for(Map.Entry<Integer, Integer> entry : counts.entrySet()){
            if(entry.getValue()==max_count){
                res = Math.min(res, ends.get(entry.getKey()) - starts.get(entry.getKey()) +1);
            }           
        }
        return res;        
    }
}