class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        left = 0
        ans = 0
        
        for i in range(len(s)):
            if s[i] in d and d[s[i]]>=left:
                left = d[s[i]]+1
            
            d[s[i]] = i
            ans = max(ans, i - left + 1)
        return ans
            