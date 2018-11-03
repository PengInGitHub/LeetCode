class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        res = set()
        for email in emails:
            local, domain = (email.split('@')[0].split('+')[0]).replace('.',''), email.split('@')[1]
            res.add(local+'@'+domain)
        return len(res)
            