# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-08-17 14:28:02
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-08-17 15:08:27


class Solution:
	def integerBreak(self, n):
		dp = [1 for i in range(n+1)]
		for i in range(2, n+1):
			for j in range(1, i):
				dp[i] = max(dp[i], j*(i-j), j*dp[i-j])
				
		return dp[n]
		
