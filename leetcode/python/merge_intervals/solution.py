# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        #lambda is a function, intervals will use key to sort
        intervals.sort(key = lambda x : x.start)
        length = len(intervals)
        res = []
        for i in range(length):
            if res == []:
                res = [intervals[i]]
            else:
                n = len(res)
                if res[n-1].start <= intervals[i].start <= res[n-1].end:
                    res[n-1].end = max(intervals[i].end, res[n-1].end)
                else:
                    res.append(intervals[i])
        return res