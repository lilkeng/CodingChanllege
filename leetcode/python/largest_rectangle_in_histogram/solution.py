'''
Case 1: current > previous (top of height stack)
Push current height and index as candidate rectangle start position.

Case 2: current = previous
Ignore.

Case 3: current < previous
Need keep popping out previous heights, and compute the candidate rectangle with 
height and width (current index - previous index). Push the height and index to stacks.
'''
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []; i = 0; area = 0
        while i < len(heights):
            if stack == [] or heights[i] > heights[stack[len(stack) - 1]]:
                stack.append(i)
                i += 1
            else:
                curr = stack.pop()
                width = i if stack == [] else (i - stack[len(stack) - 1] -1)
                area = max(area, width * heights[curr])
        while stack != []:
            curr = stack.pop()
            width = i if stack == [] else (i - stack[len(stack) - 1] -1)
            area = max(area, width * heights[curr])    
        return area