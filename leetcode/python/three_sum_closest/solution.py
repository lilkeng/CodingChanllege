class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums)-1
            while (left < right):
                tmp = nums[i] + nums[left] + nums[right]
                if abs(target - tmp) < abs(target - res):
                    res = tmp
                    
                if target < tmp:
                    right -= 1
                else:
                    left += 1
        return res