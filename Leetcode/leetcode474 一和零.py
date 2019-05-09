# -*- coding: utf-8 -*-
# @Author: Orange灬Fish
# @Date:   2019-05-09 00:33:57
# @Last Modified by:   Orange灬Fish
# @Last Modified time: 2019-05-09 00:36:39


'''
DP 定义一个数组 (m+1)*(n+1)，dp[m][n]代表m个0, n个1能组成的字符串最大数量。
遍历每个字符串统计出现的0和1得到zero和one，所以dp[i][j] = max(dp[i][j], dp[i-zero][j-one]+1)
其中dp[i-zero][j-one]表示如果取了当前的这个字符串，那么剩下的0 1可以组成的字符串最大数量。


A1：
如果对于一个字符串'10'，且 m = 2, n = 3
那么双层嵌套是为了遍历所有可以包含'10'的字符串的0 1数量组
即寻找
(2个0 3个1) (2个0 2个1) (2个0 1个1)
(1个0 3个1) (1个0 2个1) (1个0 1个1)
所能构成的字符串的最大数量
NOTE：
最后遍历到的即构成'10'本身的0 1数量组，那么通过状态转移方程这个数量组会被设为1，即dp[1][1] = 1，
列表中所有字符串的0 1数量组(i, j)都会被态转移方程设为1，即dp[i][j] = 1

那么对于遍历到的字符串0 1数量组比如(2个0 3个1):
它可以选择构成'10' -- dp[2-1][3-1]+1
或不构成 -- dp[2][3]
'''
class Solution:
	def findMaxForm(self, strs, m, n):
		# m 个 0, n 个 1
		dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
		for item in strs:
			# 统计每个字符0 1数量
			zero, one = 0, 0
			for t in item:
				if t == '0':
					zero += 1
				else:
					one += 1
			for i in range(m, zero-1, -1):
				for j in range(n, one-1, -1):
					# 此双层嵌套的意义见 A1
					dp[i][j] = max(dp[i][j],dp[i - zero][j - one] + 1)

		return dp[m][n]

