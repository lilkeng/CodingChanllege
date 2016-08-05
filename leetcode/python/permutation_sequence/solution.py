'''
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

假设n = 6，k = 400

先计算第一位，

第一位为6，那么它最少也是第5! * 5 + 1个排列，这是因为第一位为1/2/3/4/5时，都有5!个排列，因此第一位为6时，至少是第5! * 5 + 1个排列（这个排列为612345）。

5! * 5 + 1 = 601 > k，所以第一位不可能是6.

一个一个地枚举，直到第一位为4时才行，这时，4xxxxx至少为第5! * 3 + 1 = 361个排列。
'''
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        fac = 1
        for i in range(1, n):
            fac *= i
        num = [1,2,3,4,5,6,7,8,9]
        res = ''
        k -= 1 #k need to minus one
        for i in reversed(range(n)):
            curr = num[k/fac]
            res += str(curr)
            num.remove(curr)
            if i!= 0:
                # calc k first, then calc fac
                k %= fac
                fac /= i
        return res