class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '' or s[0] == '0':
            return 0
        dp = [0 for i in range(len(s)+1)]
        dp[0] = 1
        if (self.isValid(s[0])):
            dp[1] = 1
        else:
            dp[1] = 0
        
        for i in range(2, len(s)+1):
            if self.isValid(s[i-1:i]):
                dp[i] += dp[i-1]
            if self.isValid(s[i-2:i]):
                dp[i] += dp[i-2]
        return dp[len(s)]
    
    def isValid(self, sub):
        if sub[0] == '0':
            return False
        return int(sub) > 0 and int(sub)<=26
                