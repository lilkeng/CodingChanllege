class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        else:
            res = []
            for i, e in enumerate(nums):
                # nums = [1,2,3]
                #(0,1), (0,2), (0,3)
                rest = nums[:i] + nums[i + 1:]
                rest_perms = self.permute(rest)
                for perm in rest_perms:
                    perm.append(e)
                res += rest_perms
            return res