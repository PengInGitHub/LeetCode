class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if nums is None or len(nums) == 0:
            return nums
        rows, cols = len(nums), len(nums[0])
        if rows*cols != r*c:
            return nums
        
        res = []
        for i in range(rows*cols):
            ori_x, ori_y = i//cols, i%cols
            new_x, new_y = i//c, i%c
            res[new_x][new_y] = nums[ori_x][ori_y]
        return res
        