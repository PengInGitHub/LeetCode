class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = max_len = 0
        seen = {}
        for key, value in enumerate(s):
            # found a repeated value
            if value in seen:
                # update start, which is the index where sub-string starts
                # update only when the index of repeated value in seen is larger than start
                # which means if the index is smaller, we do not update start
                tmp = seen[value] + 1
                if tmp > start:
                    # update the start as one more larger than the new index
                    start = tmp

            max_len = max(max_len, key - start + 1)
                # add this char into seen, no matter it is repeated or not
            seen[value] = key
        # return when iteration is done        
        return max_len