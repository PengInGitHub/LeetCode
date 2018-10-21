class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        for word in words:
            if self.sameRow(word):
                res.append(word)
        return res
        
    def sameRow(self, word):
        row1 = "qwertyuiopQWERTYUIOP"
        row2 = "asdfghjklASDFGHJKL"
        row3 = "zxcvbnmZXCVBNM"
        
        first_ele_row = row1
        if word[0] in row2:
            first_ele_row = row2
        elif word[0] in row3:
            first_ele_row = row3
        
        for char in word:
            if char not in first_ele_row:
                return False
        return True