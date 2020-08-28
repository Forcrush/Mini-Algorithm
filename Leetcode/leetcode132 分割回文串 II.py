# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-05 19:42:38
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-05 20:41:40


# DP
# dp[i]：表示前缀子串 s[:i+1] 分割成若干个回文子串所需要最小分割次数
# dp[i] = min([dp[j] + 1 for j in range(i) if s[j+1:i+1] 是回文串])
class Solution:
	def minCut(self, s):
		
		isPalin = lambda x: x == x[::-1]

		dp = [i for i in range(len(s))]

		for i in range(len(s)):
			if isPalin(s[:i+1]):
				dp[i] = 0
				continue
			dp[i] = min([dp[j] + 1 for j in range(i) if isPalin(s[j+1:i+1])])

		return dp[len(s)-1]

