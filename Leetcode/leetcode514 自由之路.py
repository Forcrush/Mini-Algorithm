'''
Author: Puffrora
Date: 2021-03-01 14:46:17
LastModifiedBy: Puffrora
LastEditTime: 2021-03-01 20:05:10
'''


# DP
# 时间复杂度 O(m*n*n)
# 空间复杂度 O(m*n)
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        
        from collections import defaultdict

        m, n = len(key), len(ring)

        # ! dp[i][j] 表示从前往后拼写出 key 的第 i 个字符
        # ! ring 的第 j 个字符与 12: 00 方向对齐的最少步数（下标均从 00 开始）
        dp = [[float('inf') for _ in range(n)] for _ in range(m)]

        pos = defaultdict(list)
        for i, c in enumerate(ring):
            pos[c].append(i)
        
        for i in pos[key[0]]:
            dp[0][i] = min(i, n-i) + 1
        
        for i in range(1, m):
            for j in pos[key[i]]:
                for k in pos[key[i-1]]:
                    dp[i][j] = min(dp[i][j], dp[i-1][k] + min(abs(j-k), n-abs(j-k)) + 1)
        
        return min(dp[m-1])