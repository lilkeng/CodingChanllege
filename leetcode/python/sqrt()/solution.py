class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        i = 1
        j = x/2 + 1
        while i<=j:
            mid = i + (j-i)/2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 > x:
                j = mid-1
            else:
                i = mid+1
        return j
                