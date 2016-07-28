class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if nums == []:
            return 0
        if len(nums) == 1:
            return 1
        count = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[count+1] = nums[i]
                count += 1
        return count+1