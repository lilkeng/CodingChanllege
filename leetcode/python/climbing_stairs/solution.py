'''
Treat this question as fibonacci
The last stair has two way to climb: use 2 steps from n-2 or use 1 step from n-1
'''
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        fb = [1 for i in range(n+1)]
        for i in range(2, n+1):
            fb[i] = fb[i-1]+fb[i-2]
        return fb[n]