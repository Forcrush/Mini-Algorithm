# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-10-06 15:55:44
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-10-06 16:11:27


class Solution:
	def change(self, amount, coins):

		dp = [0] * (amount + 1)
		dp[0] = 1

		for c in coins:
			for a in range(c, amount+1):
				dp[a] += dp[a-c]

		return dp[amount]