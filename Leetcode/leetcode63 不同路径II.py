class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        
        if row == 1 or col == 1:
            flattenlist = sum(obstacleGrid, [])
            if 1 in flattenlist:
                return 0
            else:
                return 1
        else:
            # find 1 in the 1st row or the 1st coloumn
            maxcol = -1
            maxrow = -1
            for i in range(col):
                if obstacleGrid[0][i] == 1:
                    maxcol = i
                    break
            for j in range(row):
                if obstacleGrid[j][0] == 1:
                    maxrow = j
                    break
            dp = []
            dp.append([1]*col)
            for _ in range(row-1):
                dp.append([1] + [0]*(col-1))
            if maxcol > -1:
                for i in range(maxcol, col):
                    dp[0][i] = 0
            if maxrow > -1:
                for i in range(maxrow, row):
                    dp[i][0] = 0
                    
            for i in range(1, row):
                for j in range(1, col):
                    if obstacleGrid[i][j] == 1:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dp[i][j-1] + dp[i-1][j]
                        
            return dp[row-1][col-1]