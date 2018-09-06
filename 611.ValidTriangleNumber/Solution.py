class Solution:
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums)<3:
            return 0
        
        #sort list
        nums.sort()
        count = 0
        for third_edge_idx in range(2,len(nums)):
            #third_edge = 2, 3, ... n-1
            first_edge_idx, second_edge_idx = 0, third_edge_idx-1
            while first_edge_idx < second_edge_idx:
                if nums[first_edge_idx] + nums[second_edge_idx] > nums[third_edge_idx]:
                    count += second_edge_idx - first_edge_idx
                    second_edge_idx -= 1
                else:
                    first_edge_idx += 1
                    
        return count
                