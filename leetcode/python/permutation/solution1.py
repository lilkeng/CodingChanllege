class Solution(object):
    
    def permutation(self, list, nums):
        if len(nums) == len(list):
            return Solution.res.append(copy.copy(list))
        
        for i in range(len(nums)):
            if nums[i] in list:
                continue
            list += [nums[i]]
            self.permutation(list, nums)
            del list[-1]
    
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        Solution.res = []
        if len(nums) == 0:
            return Solution.res
            
        self.permutation([], nums)
        return Solution.res