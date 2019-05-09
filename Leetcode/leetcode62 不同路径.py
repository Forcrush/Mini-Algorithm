class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        elif m == 1 or n == 1:
            return 1
        else:
            dp = []
            dp.append([1]*m)
            for _ in range(n-1):
                dp.append([1] + [0]*(m-1))

            for i in range(1, n):
                for j in range(1, m):
                    for k in range(0, i+1):
                        dp[i][j] += dp[k][j-1]
                        
            return dp[n-1][m-1]


# Optimazation
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        elif m == 1 or n == 1:
            return 1
        else:
            dp = []
            dp.append([1]*m)
            for _ in range(n-1):
                dp.append([1] + [0]*(m-1))

            for i in range(1, n):
                for j in range(1, m):
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
                        
            return dp[n-1][m-1]