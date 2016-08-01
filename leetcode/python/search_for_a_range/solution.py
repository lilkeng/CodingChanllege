class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(nums)-1
        while l <= r:
            m = l + ((r - l)>>1)
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m -1
            else:
                res = [0, 0]
                if nums[l] == target:
                    res[0] = l
                if nums[r] == target:
                    res[1] = r
                for i in range(m, r + 1):
                    if nums[i] != target: 
                        res[1] = i - 1
                        break
                for i in range(m, l - 1, -1):
                    if nums[i] != target:
                        res[0] = i + 1
                        break
                return res
        return [-1, -1]
                
                
                
                
                