'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:
'''
class Solution(object):
    def helper(self, l, r, list, res):
        # Remaining left less than right
        if l > r:
            return
        if l == 0 and r == 0:
            res.append(list)
        if l > 0:
            self.helper(l-1, r, list+'(', res)
        if r > 0:
            self.helper(l, r-1, list+')', res)
    
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        res = []
        self.helper(n, n, '', res)
        return res