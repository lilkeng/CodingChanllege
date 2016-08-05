 '''
 试想一下，如果我们从头遍历这个数组。对于数组中的其中一个元素，它只有两个选择：

 1. 要么加入之前的数组加和之中（跟别人一组）

 2. 要么自己单立一个数组（自己单开一组）
 '''
 class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        maxSum = nums[0]
        maxCurrent = maxSum
        for i in range(1, len(nums)):
            maxCurrent = max(nums[i], maxCurrent + nums[i])
            maxSum = max(maxSum, maxCurrent)
        return maxSum