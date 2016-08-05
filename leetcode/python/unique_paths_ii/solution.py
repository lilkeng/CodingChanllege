class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        f = [[0 for i in range(m)] for j in range(n)]
        for i in range(m):
            if obstacleGrid[0][i] == 0:
                f[0][i] = 1
            else:
                f[0][i] = 0
                break
        for i in range(n):
            if obstacleGrid[i][0] == 0:
                f[i][0] = 1
            else:
                f[i][0] = 0
                break
        for i in range(1,n):
            for j in range(1,m):
                if obstacleGrid[i][j] == 1:
                    f[i][j] = 0
                else:
                    f[i][j] = f[i-1][j] + f[i][j-1]
                    
        return f[n-1][m-1]
        
        
        
        
        
        
        
                    