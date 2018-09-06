class Solution {
  public:
    int triangleNumber(vector < int > & nums) {

      if (nums.size() < 3) return 0;
      sort(nums.begin(), nums.end());
      int count = 0;
      for (int third_edge = 2; third_edge < nums.size(); third_edge++) {
        int first_edge = 0, second_edge = third_edge - 1;
        while (first_edge < second_edge) {
          if (nums[first_edge] + nums[second_edge] > nums[third_edge]) {
            count += second_edge - first_edge;
            second_edge--;
          } else {
            first_edge++;
          }
        }
      }
      return count;
    }
};