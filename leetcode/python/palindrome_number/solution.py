'''
Determine whether an integer is a palindrome. Do this without extra space.

Some hints:
Could negative integers be palindromes? (ie, -1)
'''
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        #reverse it and compare
        if x < 0:
            return False
        tmp = x 
        res = 0
        while tmp>0:
            res = res * 10 + tmp % 10
            tmp = tmp / 10
        return res == x