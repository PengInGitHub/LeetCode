class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        A, B = A.split(), B.split()
        return [x for x in A if A.count(x) == 1 and x not in B] + [x for x in B if B.count(x) == 1 and x not in A]
        