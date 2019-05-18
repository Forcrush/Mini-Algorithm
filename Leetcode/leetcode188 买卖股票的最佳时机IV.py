# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-05-15 00:08:57
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-05-15 00:20:02


'''
当k大于等于数组长度一半时, 问题退化为贪心问题此时采用
买卖股票的最佳时机II 的贪心法解决可以大幅提升时间性能
对于其他的k, 可以采用 买卖股票的最佳时机III 的方法来解决
'''
class Solution:
	def maxProfit(self, k, prices):
		if prices == []:
			return 0
			
		if k >= len(prices)/2:
			profits = 0
			for i in range(1, len(prices)):
				if prices[i] > prices[i-1]:
					profits += prices[i] - prices[i-1]
			return profits

		# dp[i][j][0]表示第i天交易了j次时不持有股票, dp[i][j][1]表示第i天交易了j次时持有股票
		dp = [[[0 for _ in range(2)] for _ in range(k+1)] for _ in range(len(prices))]
		for i in range(k+1):
			dp[0][i][0], dp[0][i][1] = 0, -1 * prices[0]

		for i in range(1, len(prices)):
			for j in range(k+1):
				if j == 0:
					dp[i][j][0] = dp[i-1][j][0]
				else:
					dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j-1][1] + prices[i])
				dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j][0] - prices[i])

		maxpro = dp[len(prices)-1][0][0]
		for i in range(1, k+1):
			maxpro = max(maxpro, dp[len(prices)-1][i][0])
		return maxpro