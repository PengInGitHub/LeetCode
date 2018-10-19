class Solution(object):
    
    def selfDividingNumbers1(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for num in range(left, right+1):
            # get each unit of num, and divide by num itself, check if equals to zero
            flag_valid = True
            tmp = num
            while num > 0:
                unit = num%10
                if unit == 0 or tmp%unit != 0:
                    flag_valid = False
                num /= 10
            if flag_valid:
                res.append(tmp)
        return res

    def selfDividingNumbers(self, left, right):
        res =  []
        for num in range(left, right+1):
            ori, valid = num, True
            while num > 0:
                unit = num % 10
                if unit == 0 or ori%unit != 0:
                    valid = False              
                num /= 10
            if valid:
                res.append(ori)
        return res