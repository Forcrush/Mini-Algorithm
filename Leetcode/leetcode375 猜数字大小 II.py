# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-09-18 23:10:23
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-09-18 23:36:37

'''
dp(i, j) 代表答案在 (i, j) 中最坏情况下最小开销的代价
dp(i,j)	= 	min 	(pivot + max(dp(i, pivot−1), dp(pivot+1, n)))
		pivots(i,j)
'''
class Solution:
	def getMoneyAmount(self, n):
		dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

		for length in range(2, n+1):
			for start in range(1, n+1 - length + 1):
				tmp = float('inf')
				for pivot in range(start, start+length-1):
					res = pivot + max(dp[start][pivot-1], dp[pivot+1][start+length-1])
					tmp = min(tmp, res)
				dp[start][start+length-1] = tmp

		return dp[1][n]

'''
Solution().getMoneyAmount(10) = 16
这题不是按照二分法
如果 n = 10，先猜7，再依据大小猜9或4，如果猜9再不对，那一定是8或10，花费7+9=16
如果是猜4不对再往下猜也不会超过16，所以如果是n=10，结果是16.
'''