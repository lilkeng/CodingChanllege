'''
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.


'''
class Solution(object):
    def firstMissingPositive(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        n = len(A)
        if n == 0: return 1
        while i < n:
            while A[i] != i+1 and A[i] <= n and A[i] > 0 and A[i] != A[A[i]-1]:
                temp = A[i]
                A[i] = A[A[i]-1]
                A[temp-1] = temp #Be careful the A[i] got changed, don't use it!!
            i += 1
        for i in range(n):
            if A[i] != i+1:
                return i+1
        return n+1
                