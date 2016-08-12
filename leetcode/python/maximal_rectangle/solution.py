class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == []:
            return 0
        a = [0 for i in range(len(matrix[0]))]
        maxArea = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                a[j] = a[j] + 1 if matrix[i][j] == '1' else 0
            # Notice: updata maxArea for each row
            maxArea = max(maxArea, self.largestRectangleArea(a))
        return maxArea
        
        
    def largestRectangleArea(slef, heights):
        stack = []; i = 0; area = 0
        while i < len(heights):
            if stack==[] or heights[i]>heights[stack[len(stack)-1]]:
                stack.append(i)
                i += 1
            else:
                #pop stack until height[i] > height[stack[len(stack)-1]]
                #the width is from the i to the stack[len(stack)-1]
                #because if height[i] > height[i-1] it will append i 
                #but if height[i] <= height[i-1] it will pop out so the first curr is always i-1
                #height in stack [3,4,2,1,5] won't exist bc it is no meaning to keep the higher height in the heights
                #height in stack always will be small to big from left to right
                curr = stack.pop()
                width = i if stack == [] else i - stack[len(stack) - 1] - 1
                area = max(area, heights[curr] * width)
        if stack != []:
            curr = stack.pop()
            width = i if stack == [] else i - stack[len(stack) - 1] - 1
            area = max(area, heights[curr] * width)
        return area
    