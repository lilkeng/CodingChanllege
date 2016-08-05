'''
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).


先将矩阵转置，然后将矩阵的每一行翻转，就可以得到所要求的矩阵了
'''
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            #j start from i+1, bc [i][i] won't change, axis of symmetry.
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()