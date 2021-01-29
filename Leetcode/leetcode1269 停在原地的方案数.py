'''
Author: Puffrora
Date: 2021-01-29 12:26:19
LastModifiedBy: Puffrora
LastEditTime: 2021-01-29 12:39:50
'''


"""
DP
dp[i][j] 表示经过 i 次移动后在位置 j 的方案数

因为每次可以有 向左 向右 不动 三种选择
dp[i][j] = dp[i-1][j] + dp[i-1][j-1] + dp[j+1]

空间优化后只需要一维dp数组 注意 j >= 0
"""
class Solution:
    def numWays(self, steps, arrLen):
        
        # 剪枝
        arrLen = min(arrLen, steps+1)
        
        pre = [1] + [0] * (arrLen - 1)

        for _ in range(steps):
            cur = [0] * arrLen
            for j in range(arrLen):
                for k in [-1, 0, 1]:
                    if 0 <= j+k < arrLen:
                        cur[j] += pre[j+k]
            pre = cur
        
        return pre[0] % (10 ** 9 + 7)
