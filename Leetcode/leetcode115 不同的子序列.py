# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-13 15:00:27
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-13 15:09:38


class Solution:
	def numDistinct(self, s, t):

		# s是母串 t是子串 
		# dp[i][j] 表示 s 的前 j 个字母可通过 t 前 i 个字母组成的数量
		dp =[[0 for _ in range(len(s)+1)] for _ in range(len(t)+1)]
		
		# 可由空串
		for i in range(len(s)+1):
			dp[0][i] = 1

		for i in range(1, len(t)+1):
			for j in range(1, len(s)+1):
				if t[i-1] == s[j-1]:
					dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
				else:
					dp[i][j] = dp[i][j-1]

		return dp[len(t)][len(s)]