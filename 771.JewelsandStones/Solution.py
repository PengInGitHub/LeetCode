#ref
#https://stackoverflow.com/questions/538346/iterating-over-a-string
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        for j in J:
            for s in S:
                if j==s:
                    count += 1
        return count
        