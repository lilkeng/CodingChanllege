'''
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.
'''
class Solution(object):
    def count(self, s):
        tmp = ''; count = 0; curr = '#' 
        for i in s:
            if i != curr:
                if curr != '#':
                    tmp += str(count) + curr
                count = 1
                curr = i
            else:
                count += 1
        tmp += str(count) + curr
        return tmp
            
    def countAndSay(self, n):
        s = '1'
        for i in range(2, n+1):
            s = self.count(s)
        return s