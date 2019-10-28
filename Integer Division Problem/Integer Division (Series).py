# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-10-28 10:05:19
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-10-28 11:15:50


'''
整数划分问题 (此系列是求划分数而非划分组合)
1. 将 n 划分成若干正整数之和的划分数
2. 将 n 划分成 k 个正整数之和的划分数
3. 将 n 划分成最大数不超过 k 的划分数 (划分组合中不同数最多为k)
4. 将 n 划分成若干奇正整数之和的划分数
5. 将 n 划分成若干不同正整数之和的划分数

定义 dp[i][j] 为整数 i 被划分成 j 个数的划分数

dp[i][j] = dp[i-j][j] + dp[i-1][j-1]

第一项表示分解的数不含1 即每个数减去1得到i-j 划分成j个数
第二项表示分解的数含1
'''
# 假设最大 n 为 100
N = 100
dp = [[0]*N] * N
dp2 = [[0]*N] * N


def divide1_method1(n):
	for i in range(1, n+1):
		for j in range(1, i+1):
			if j == 1:
				dp[i][j] = 1
			else:
				dp[i][j] = dp[i-j][j] + dp[i-1][j-1]

	return dp[n][n]


def divide2(n, k):
	for i in range(1, n+1):
		for j in range(1, max(i, k)+1):
			if j == 1:
				dp[i][j] = 1
			else:
				dp[i][j] = dp[i-j][j] + dp[i-1][j-1]

	return dp[n][k]


def divide3_method1(n, k):
	for i in range(1, n+1):
		for j in range(1, i+1):
			if j == 1:
				dp[i][j] = 1
			else:
				dp[i][j] = dp[i-j][j] + dp[i-1][j-1]

	# sigma(dp[n][i]) 1<=i<=k
	res = 0
	for i in range(1, k+1):
		res += dp[n][i]

	return res

==================================incomplete below
'''
定义 dp2[i][j] 为 i 的划分最大数为 j 的划分数

dp2[i][j] = dp2[i-j][j] + dp[i][j-1]

第一项表示每种情况都含至少一个最大数j 则先保留一个j 对剩下的i-j划分 最大数仍为j
第二项表示划分数所有数都小于j的情况数
'''
def divide1_method2(n):
	for i in range(0, n+1):
		for j in range(1, n+1):
			if i < j:
				dp2[i][j] = dp2[i][i]
			if i == j:
				# 1 即为 i 自身
				dp2[i][j] = dp2[i][j-1] + 1 
			if i > j:
				dp2[i][j] = dp2[i-j][j] + dp2[i][j-1]

	return dp2[n][n]


def divide3_method2(n, k):
	for i in range(0, n+1):
		for j in range(1, n+1):
			if i < j:
				dp2[i][j] = dp2[i][i]
			if i == j:
				# 1 即为 i 自身
				dp2[i][j] = dp2[i][j-1] + 1 
			if i > j:
				dp2[i][j] = dp2[i-j][j] + dp2[i][j-1]

	return dp2[n][k]

