class Solution:
    # @return a string
    def getlongestpalindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1 : r]
    def longestPalindrome(self, s):
        palindrome = ''
        for i in range(len(s)):
            l1 = self.getlongestpalindrome(s, i, i)
            if len(l1) > len(palindrome): palindrome = l1
            l2 = self.getlongestpalindrome(s, i, i + 1)
            if len(l2) > len(palindrome): palindrome = l2
        return palindrome