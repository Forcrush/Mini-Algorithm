# -*- coding: utf-8 -*-
# @Author: Orange灬Fish
# @Date:   2019-08-09 21:34:47
# @Last Modified by:   Orange灬Fish
# @Last Modified time: 2019-08-09 21:40:11


class Solution(object):
	def numSquares(self, n):
		dp = [0] * (n + 1)
		for i in range(1, n+1):
			# i = 1 + 1 + ... = 1 * i
			dp[i] = i
			j = 1
			while j**2 <= i:
				dp[i] = min(dp[i], dp[i-j**2] + 1)
				j += 1
		return dp[-1]