'''
Author: Puffrora
Date: 2021-01-26 20:04:42
LastModifiedBy: Puffrora
LastEditTime: 2021-01-26 20:17:53
'''


class Solution:
    def countSquares(self, matrix):

        row, col = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]

        res = 0
        for i in range(row):
            for j in range(col):
                if i == 0 or j == 0:
                    dp[i][j] = matrix[i][j]
                elif matrix[i][j]:
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                
                res += dp[i][j]
        
        return res

