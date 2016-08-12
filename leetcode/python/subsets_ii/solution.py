'''
Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.
'''
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == [] or len(nums) == 0:
            return []
        self.res = []
        nums.sort()
        self.helper(nums, 0, [])
        return self.res
        
    def helper(self, nums, start, list):
        self.res.append(list[:])
        for i in range(start, len(nums)):
            if i != start and nums[i] == nums[i-1]:
                continue
            list.append(nums[i])
            self.helper(nums, i+1, list)
            list.pop()
            