class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        count = 0
        for i in range(31):
            bin_x, bin_y = x%2, y%2
            if bin_x != bin_y:
                count += 1
            x, y = x//2, y//2
        return count
                
        
        