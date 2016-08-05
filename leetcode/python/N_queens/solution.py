class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.n = n
        Solution.res = []
        columns = [-1 for i in range(n)]
        self.solve(columns, 0)
        return Solution.res
    
    def solve(self, columns, row):
        if row == self.n:
            Solution.res.append(self.generate_list(columns))
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
        return True #be careful the position of return
            
    def generate_list(self, columns):
        sol = []
        row = ['.' for i in range(self.n)]
        for i in columns:
            new_row = row[:]
            new_row[i] = 'Q'
            sol.append(''.join(new_row))
        return sol
