'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

'''
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for index in range(len(nums)-2):
            if index and nums[index] == nums[index-1]:
                continue
            l = index + 1
            r =  len(nums)-1
            # l can't be equal to r
            while (l<r):
                if nums[index] + nums[l] +nums[r] == 0:
                    res.append([nums[index], nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while l<r and nums[l] == nums[l-1]:
                        l += 1
                    while l<r and nums[r] == nums[r+1]:
                        r -= 1
                elif nums[l]+nums[r] < -nums[index]:
                    l += 1
                else:
                    r -= 1
        return res