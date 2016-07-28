class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        '''
        Try to put all the elem to the end of the array,
        we have two pointer: one is the elem from last,
        one is the position gonna be the elem also from last.
        if the first elem pointer equals to elem
        change the position with second pointer,
        So in the end, j is the last position not equals to elem, return j+1 which is the length
        '''
        j = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            if nums[i]  == val:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
        return j + 1