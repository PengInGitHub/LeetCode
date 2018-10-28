from collections import Counter
class Solution(object):
    def singleNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            print('before', res, 'num', num)
            res = res ^ num
            print('after', res)            
        return res

    def singleNumber(self, nums):
        b = Counter(nums).most_common()[::-1]
        return b[0][0]
        
