class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.n = n
        self.res = 0
        columns = [-1 for i in range(n)]
        self.solve(columns, 0)
        return self.res
    
    def solve(self, columns, row):
        if row == self.n:
            self.res += 1
            
        else:
            for col in range(self.n):
                if self.isValid(columns, row, col):
                    columns[row] = col
                    self.solve(columns, row+1)
                    
                    
    def isValid(self, columns, row, col):
        for r in range(row):
            c = columns[r]
            if c == col:
                return False
            if abs(c - col) == row - r:
                return False
        return True