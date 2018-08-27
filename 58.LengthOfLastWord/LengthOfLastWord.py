class Solution(object):
    def lengthOfLastWord(self, s):
        if ' ' in s:
            if s == ' ':
                return 0
            s = s.strip()
            return len(s[s.rfind(' ')+1:])
        return len(s)

#resource
#https://stackoverflow.com/questions/9572490/find-index-of-last-occurrence-of-a-substring-in-a-string
#https://stackoverflow.com/questions/663171/is-there-a-way-to-substring-a-string-in-python
#https://stackoverflow.com/questions/761804/how-do-i-trim-whitespace-from-a-python-string