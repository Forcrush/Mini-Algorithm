# -*- coding: utf-8 -*-
# @Author: Orange灬Fish
# @Date:   2019-05-08 00:08:22
# @Last Modified by:   Orange灬Fish
# @Last Modified time: 2019-05-08 00:15:54


# DP: 第i天最大利润 = max(前i-1天最大利润, 第i天价格-前i天最低价格)
class Solution:
	def maxProfit(self, prices):
		if prices == []:
			return 0
		minprice = prices[0]
		maxprofit = -1
		for i in prices:
			minprice = min(minprice, i)
			maxprofit = max(maxprofit, i - minprice)
		return maxprofit