'''
Don't forget to sort first !!!!!!!!
'''
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums)-3):
            if i and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j!= i+1 and nums[j] == nums[j-1]:
                    continue
                left = j+1
                right = len(nums)-1
                sum = target - (nums[i] + nums[j])
                while left < right:
                    if sum == nums[left] + nums[right]:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        right -= 1
                        left += 1
                        while (left < right and nums[left] == nums[left-1]):
                            left += 1
                        while (left < right and nums[right] == nums[right+1]):
                            right -= 1
                    elif sum < nums[left] + nums[right]:
                        right -= 1
                        
                    else:
                        left += 1
        return res