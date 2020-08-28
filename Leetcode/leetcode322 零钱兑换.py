# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-19 16:24:05
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-19 16:51:37


class Solution:
	def coinChange(self, coins, amount):

		dp = [float("inf")] * (amount + 1)
		dp[0] = 0

		for c in coins:
			for i in range(c, amount+1):
				dp[i] = min(dp[i], dp[i-c]+1)

		return dp[amount] if dp[amount] != float("inf") else -1

