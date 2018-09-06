import java.util.Arrays;

class Solution {
    public int triangleNumber(int[] nums) {
        if(nums == null || nums.length == 0)return 0;
        
        int counter = 0;
        //sort list
        Arrays.sort(nums);
        //iterate the array from the 2nd value
        
        for (int third_edge_idx=2; third_edge_idx<nums.length; third_edge_idx++){
            int first_edge_idx = 0;
            int second_edge_idx = third_edge_idx-1;
            while (first_edge_idx<second_edge_idx){
                if (nums[first_edge_idx] + nums[second_edge_idx] > nums[third_edge_idx]){
                    counter += second_edge_idx-first_edge_idx;
                    second_edge_idx--;
                }else{
                    first_edge_idx++;
                }
            }
            
        }
        return counter;  
    }
}