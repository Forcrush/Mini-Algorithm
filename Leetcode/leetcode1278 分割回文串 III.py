'''
Author: Puffrora
Date: 2021-02-23 19:45:25
LastModifiedBy: Puffrora
LastEditTime: 2021-02-23 20:00:21
'''


# 时间复杂度 O(N*N*K)
# 空间复杂度 O(N*N + N*K)
class Solution:
    def palindromePartition(self, s, k):

        n = len(s)

        # cost[i][j] 记录将 s[i:j+1] 变成回文串需要的最小修改次数
        cost = [[0 for _ in range(n)] for _ in range(n)]
        for span in range(2, n+1):
            for i in range(n-span+1):
                j = i + span - 1
                cost[i][j] = cost[i+1][j-1] + (0 if s[i] == s[j] else 1)
        
        # dp[i][j] 表示对于字符串 s 的前 i 个字符，将它分割成 j 个非空且不相交的回文串 最少需要修改的字符数
        dp = [[float('inf') for _ in range(k+1)] for _ in range(n+1)]
        dp[0][0] = 0
        for i in range(1, n+1):
            for j in range(1, min(k, i)+1):
                if j == 1:
                    dp[i][j] = cost[0][i-1]
                else:
                    for t in range(j-1, i):
                        dp[i][j] = min(dp[i][j], dp[t][j-1] + cost[t][i-1])
        
        return dp[n][k]