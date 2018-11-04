class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s[::-1]
        s = s.split()[::-1]        
        return ' '.join(s)
        
    def reverseWords2(self, s):
        # Write your code here
        return ' '.join([x[::-1] for x in s.split()])