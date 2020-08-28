# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-15 00:12:22
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-15 00:41:50


'''
我们用 f(i, j) 表示数字 [1 .. i] 的排列中恰好包含 j 个逆序对的个数 在状态转移时，
我们考虑数 i 放置的位置与逆序对个数的关系。我们在数字 [1 .. i - 1] 组成的排列中放入 i 时，
有 i 种放置方法：如果将 i 放在最后，则逆序对数量不变；如果将 i 放在倒数第二个，则逆序对数量增加 1；
如果将 i 放在第一个，则逆序对数量增加 i - 1。这是因为 i 是 [1 .. i] 中的最大值，
因此将它放置在 [1 .. i - 1] 的排列中的任意一个位置，它都会与在它之后的那些数形成逆序对。
如果它后面有 k 个数，则会形成 k 个逆序对。

f(i, j) = f(i - 1, j) + f(i - 1, j - 1) + ... + f(i - 1, j - i + 1)
容易得到 f(i, j - 1) = f(i - 1, j - 1) + f(i - 1, j - 2) + ... + f(i - 1, j - i)
即
f(i, j) - f(i - 1, j) = f(i, j - 1) - f(i - 1, j - i)
==> f(i, j) = f(i, j - 1) + f(i - 1, j) - f(i - 1, j - i)

'''
class Solution:
	def kInversePairs(self, n, k):
		dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

		for i in range(n+1):
			dp[i][0] = 1

		for i in range(2, n+1):
			for j in range(1, k+1):
				tmp = 0 if j-i < 0 else dp[i-1][j-i]
				dp[i][j] = dp[i-1][j] + dp[i][j-1] - tmp
		print(dp)

		return dp[n][k] % 1000000007

