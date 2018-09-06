class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count = -sys.maxsize
        #create 3 dict 
        #starts and ends are to store where (at which index) the num first and last time shows up in the num
        #counts is to store the frequency a num (key) shows up (value)
        starts, ends, counts  = {}, {}, {}
        
        for i, num in enumerate(nums):
            #num shows up for the very first time
            if num not in starts:
                starts[num] = i
                counts[num] = 0
            #it is not the first time that num shows up
            counts[num] += 1
            ends[num] = i
            #update max_count, the final value of max_count would be the degree of array
            max_count = max(max_count, counts[num])
        
        #create var to store the return value
        res = sys.maxsize
        #iterate dict: k, v in my_dict.items()
        for num, count in counts.items():
            #found the num(num) with the degree of array(count)
            if count == max_count:
                res = min(res, ends[num]-starts[num]+1)
        return res
                
                