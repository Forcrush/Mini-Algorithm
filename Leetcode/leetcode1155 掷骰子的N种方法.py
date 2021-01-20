'''
Author: Puffrora
Date: 2021-01-20 19:39:53
LastModifiedBy: Puffrora
LastEditTime: 2021-01-20 21:02:50
'''
# DP dp[i][j] 表示 i 个骰子 target为 j 时的组合数
class Solution:
    def numRollsToTarget(self, d, f, target):
        
        dp = [[0 for _ in range(target+1)] for _ in range(d+1)]

        for j in range(1, target+1):
            dp[1][j] = 1 if j <= f else 0

        for i in range(2, len(dp)):
            for j in range(1, len(dp[0])):
                for n in range(min(f, j), 0, -1):
                    dp[i][j] += dp[i-1][j-n]
                    
        return dp[d][target] % (10 ** 9 + 7)

