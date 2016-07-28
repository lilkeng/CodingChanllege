class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0; h = len(nums)-1
        while l <= h:
            m = l + ((h-l)>>1) # important to add parenthese!!!
            if nums[m] == target:
                return m
            elif (nums[l] < nums[m] and target >= nums[l] and target < nums[m]) or (nums[l] > nums[m] and not (target > nums[m] and target <= nums[h])):
                h = m -1
            else:
                l = m + 1
        return -1