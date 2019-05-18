# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-05-14 22:14:01
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-05-15 00:08:27


class Solution:
	def maxProfit(self, prices):
		if prices == []:
			return 0
		# dp[i][j][0]表示第i天交易了j次时不持有股票, dp[i][j][1]表示第i天交易了j次时持有股票
		dp = [[[0 for _ in range(2)] for _ in range(3)] for _ in range(len(prices))]
		for i in range(3):
			dp[0][i][0], dp[0][i][1] = 0, -1 * prices[0]

		for i in range(1, len(prices)):
			for j in range(3):
				if j == 0:
					dp[i][j][0] = dp[i-1][j][0]
				else:
					dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j-1][1] + prices[i])
				dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j][0] - prices[i])

		return max(dp[len(prices)-1][0][0], dp[len(prices)-1][1][0], dp[len(prices)-1][2][0])

