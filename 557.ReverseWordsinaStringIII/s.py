class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s[::-1]
        s = s.split()[::-1]        
        return ' '.join(s)
        