class Solution(object):
    
    def findKth(self, A, B, k):
        len1 = len(A)
        len2 = len(B)
        if(len1 > len2): return self.findKth(B, A, k)
        if(len1 == 0): return B[k-1]
        if(k==1): return min(A[0], B[0])
        pa = min(len(A), k/2); pb = k-pa
        if(A[pa-1] <= B[pb-1]):
            return self.findKth(A[pa:], B, pb)
        else:
            return self.findKth(A, B[pb:], pa)
            
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        k = len1 + len2
        if(k%2 == 1): 
            return self.findKth(nums1, nums2, k/2+1)
        else:
            return (self.findKth(nums1, nums2, k/2) + self.findKth(nums1, nums2, k/2+1)) * 0.5