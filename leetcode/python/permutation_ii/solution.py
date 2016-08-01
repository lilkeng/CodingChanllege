'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
'''
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.permute(sorted(nums)) #Using sorted(nums), it can return the sorted list; list.sort() just sort it in place
        
    def permute(self, nums):
        if not nums:
            return [[]]
        else:
            res = []
            prev = None
            for i, e in enumerate(nums):
                if prev == None or prev != e:
                    rest = nums[:i] + nums[i+1:]
                    rest_perms = self.permute(rest)
                    for perm in rest_perms:
                        perm.append(e)
                    res += rest_perms
                    prev = e
        return res
            