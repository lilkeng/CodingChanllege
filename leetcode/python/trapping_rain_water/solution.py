'''
Given n non-negative integers representing an elevation map where the 
width of each bar is 1, compute how much water it is able to trap after 
raining.
'''
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n == 0: return 0
        pos = []
        neg = []
       
        p = q = 0
        pos.append(p)
        while q < n-1:
            q += 1
            if height[q] >= height[p]:
                pos.append(q) # if the height got greater than the former record, save its position
                p = q
        
        p = q = n-1
        neg.append(p)
        while q > 0:
            q -= 1
            if height[q] > height[p]:
                neg.append(q)
                p = q
        
        ans = 0
        for i in range(len(pos) - 1):
            for j in range(pos[i] + 1, pos[i+1]):
                ans += height[pos[i]] - height[j]
        
        for i in range(len(neg) - 1):
            for j in range(neg[i] - 1, neg[i+1], -1):
                ans += height[neg[i]] - height[j]
        
        return ans