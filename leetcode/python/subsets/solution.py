class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        self.DFS(nums, 0, [])
        return self.res
    
    def DFS(self, nums, start, list):
        self.res.append(list[:])
        if len(list) == len(nums):
            return
        for i in range(start, len(nums)):
            list.append(nums[i])
            self.DFS(nums, i + 1, list)
            list.pop()