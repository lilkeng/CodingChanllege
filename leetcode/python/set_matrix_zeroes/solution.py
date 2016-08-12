'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
'''
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rowNum = len(matrix)
        colNum = len(matrix[0])
        col = [False for i in range(rowNum)]
        row = [False for i in range(colNum)]
        for i in range(rowNum):
            for j in range(colNum):
                if matrix[i][j] == 0:
                    col[i] = True
                    row[j] = True
        for i in range(rowNum):
            for j in range(colNum):
                if col[i] == True or row[j]==True:
                    matrix[i][j] = 0
                    