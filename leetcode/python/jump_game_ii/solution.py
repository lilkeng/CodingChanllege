'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)


'''
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last = 0 # Distance has been reached
        ret = 0 # Minimum steps used 
        curr = 0 # Distance can be reached by using ret+1 step
        for i in range(len(nums)):
            if i > last: # when the range is out of the has been reached distance(p + nums[p])
                last = curr #update the maximum can be reached distance during going through [p, i]
                ret += 1
            curr =  max(curr, i+nums[i]) # calc the can be reached distance going through [p, i]
        return ret