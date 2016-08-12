'''
n = 0时，[0]

n = 1时，[0,1]

n = 2时，[00,01,11,10]

n = 3时，[000,001,011,010,110,111,101,100]
'''
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        
        result = self.grayCode(n-1)
        res = list(result) # copy
        for i in reversed(result):
            res.append(1<<(n-1) | i)
        return res