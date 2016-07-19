"""
1. Two Sum

"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        l = len(nums)
        
        i=0
        for num in nums:
            d[num] = i
            i = i+1
            
        for j in range(l):
            rest = target - nums[j]
            if rest in d:
                key = d[rest]
                if j != key:
                    break
                
        return [j, key]

