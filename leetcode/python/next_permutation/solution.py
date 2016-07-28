'''
解题思路：输出字典序中的下一个排列。比如123生成的全排列是：123，132，213，231，312，321。
那么321的next permutation是123。下面这种算法据说是STL中的经典算法。在当前序列中，从尾端往
前寻找两个相邻升序元素，升序元素对中的前一个标记为partition。然后再从尾端寻找另一个大于
partition的元素，并与partition指向的元素交换，然后将partition后的元素
（不包括partition指向的元素）逆序排列。比如14532，那么升序对为45，partition指向4，
由于partition之后除了5没有比4大的数，所以45交换为54，即15432，然后将partition之后的元素逆序排列，
即432排列为234，则最后输出的next permutation为15234。确实很巧妙。
'''
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # if len(nums) <= 1:
        #     nums
        partition = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                partition = i
                break
        if partition == -1:
            # Doesn't have ascending pairs
            nums.reverse()
        else:
            for i in range(len(nums)-1, partition, -1):
                # change the position of partition and the one greater than it
                # Because we are finding from the last one, and bc the array is descending, so the one we find is the first 
                # elem that is greater than partition
                if nums[i] > nums[partition]:
                    nums[i], nums[partition] = nums[partition], nums[i]
                    break
            # reverse the decsending array
            nums[partition+1:len(nums)] = nums[partition+1:len(nums)][::-1]
        