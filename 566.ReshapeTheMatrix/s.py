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

import numpy as np

class Solution(object):
    def matrixReshape1(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if not nums or r*c != len(nums)*len(nums[0]):
            return nums
        
        return np.reshape(nums, (r,c)).tolist()
        
    def matrixReshape(self, nums, r, c):
        if not nums:
            return nums
        
        height, width = len(nums), len(nums[0])
        
        if width * height != r * c:
            return nums
        
        i_row_new = i_col_new = 0
        
        res = [[0 for x in range(c)]for j in range(r)]
        print(res)
        
        for i_row_ori in range(height):
            for i_col_ori in range(width):
                print(i_row_new, i_col_new, i_row_ori,i_col_ori)
                res[i_row_new][i_col_new] = nums[i_row_ori][i_col_ori]
                i_col_new += 1
                if i_col_new == c:
                    i_row_new += 1
                    i_col_new = 0
        
        return res
        
    def matrixReshape2(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        x = len(nums)
        y = len(nums[0])
        rows = 0
        cols = 0
        temp = [[0 for j in range(0,c)] for i in range(0,r)]
        if r*c == x * y:
            for i in range(len(nums)):
                for j in range(len(nums[0])):
                    temp[rows][cols] = nums[i][j]
                    cols += 1
                    if cols == c:
                        rows += 1
                        cols = 0
            return temp
        else:
            return nums        
